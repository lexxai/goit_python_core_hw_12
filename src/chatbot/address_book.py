from collections import UserDict
from chatbot.record import Record
import csv
import pickle
from  pathlib import Path


class AddressBook(UserDict):

    def __init__(self, records_per_page :int = 10, 
                 default_filename :str = "chatboot_addresbook",
                 id: str = None,
                 auto_backup: bool = True,
                 auto_restore: bool = True,
                 *args, **kwargs):
        self.max_records_per_page = records_per_page
        self.default_filename = default_filename
        self.auto_backup = auto_backup
        self.auto_restore = auto_restore
        self.id = id
        super().__init__(self, *args, **kwargs)
        

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
        return True
        
    
    def get_record(self, key) -> Record:
        return self.data[key]


    def remove_record(self, key) -> None:
        del self.data[key]
        return True

    def search(self, pattern: str) -> str:
        result = []
        for r in self.data.values():
            if r.search_name_phone(pattern):
                result.append(str(r))
        return "\n".join(result)


    def clear(self) -> None:
        self.data.clear()
        return True


    def len(self):
        return len(self.data)


    def __repr__(self) -> str:
        return str(self)


    def get_csv(self) -> str:
        result = [Record.get_data_header()]
        result.extend([ str(r.get_csv_row()) for r in self.data.values() ])
        return "\n".join(result)

    
    def export_data(self) -> list:
        return [r.export_data() for r in self.data.values()]

     
    def _gen_filename(self, filename: str) -> str:
        if self.id:
            filename = f"{self.id}_{filename}"
        return filename

    def _clean_filename(self, filename: str) -> str:
        if self.id and self.id in filename:
            filename = filename[len(self.id)+1:]
        return filename


    def export_csv(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        if filename and any(self.keys()):
            try:
                with open(self._gen_filename(filename), "w", newline='') as csv_file:
                    fieldnames = Record.get_data_header_list()
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    rows = self.export_data()
                    if len(rows):
                        csv_writer.writeheader()
                        csv_writer.writerows(rows)
                return f'Exported successfully to "{filename}" file'
            except Exception:
                return False
        else:
            return False


    def import_csv(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        result = False
        if filename:
            try:
                with open(self._gen_filename(filename), "r") as csv_file:
                    fieldnames = Record.get_data_header_list()
                    csv_reader = csv.DictReader(
                        csv_file, fieldnames=fieldnames)
                    if csv_reader:
                        for csv_row in csv_reader:
                            if csv_reader.line_num == 2:
                                self.clear()     
                            if csv_reader.line_num >= 2:
                                record = Record()
                                if record.import_data(csv_row):
                                    self.add_record(record)
                        result = True
            except (FileNotFoundError, ValueError):
                ...
        return result

    def _split_line_by_commas(self, line):
        parts = []
        current_part = ''
        inside_quotes = False

        for char in line:
            if char == ',' and not inside_quotes:
                parts.append(current_part.strip())
                current_part = ''
            elif char == '"':
                inside_quotes = not inside_quotes
            else:
                current_part += char

        parts.append(current_part.strip())
        return parts

    def backup_data(self, version=None):
        if version:
            filename = f"{self.default_filename}_{version}.bin"
        else:
            filename = f"{self.default_filename}.bin"
        with open(self._gen_filename(filename), "wb") as file:
            pickle.dump(self, file)
        return True

    def restore_data(self, version=None):
        if version:
            filename = f"{self.default_filename}_{version}.bin"
        else:
            filename = f"{self.default_filename}.bin"
        with open(self._gen_filename(filename), "rb") as file:
            content = pickle.load(file)
            if type(content) == type(self):
                self.__dict__.update(content.__dict__)
                return True
        
    def list_versions(self):
        filename = f"{self.default_filename}_*.bin"
        list_files = Path('.').glob(self._gen_filename(filename))
        result_version = []
        for found_file in list_files:
            result_version.append("version: {}".format(found_file.stem.split("_")[-1]))
        return "\n".join(result_version) if any(result_version) else True
    
    def list_csv(self):
        filename = "*.csv"
        list_files = Path('.').glob(self._gen_filename(filename))
        result_version = []
        for found_file in list_files:
            result_version.append(self._clean_filename(found_file.name))
        return "\n".join(result_version) if any(result_version) else True
    

    def __export_csv_custom(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        if filename and any(self.keys()):
            with open(self._gen_filename(filename), "w") as f:
                string = self.get_csv()
                f.write(string)
            return f"saved to filename : {filename}"
        else:
            return False     


    def __import_csv_custom(self, *args) -> str:
        if len(args) and args[0]:
            filename = args[0]
        else:
            filename = self.default_filename + ".csv"
        result = False
        if filename:
            try:
                with open(self._gen_filename(filename), "r") as f:
                    csv_head = f.readline().strip().split(",")
                    if len(csv_head):
                        self.clear()
                        csv_text = f.readlines()
                        csv_head_known = {}
                        known_columns = Record.get_data_header_list()
                        for k_col in known_columns:
                            csv_head_known[k_col] = csv_head.index(k_col)
                        for line in csv_text:
                            line_field = self._split_line_by_commas(line.strip())
                            csv_row = {}
                            try:
                                for k_col in known_columns:
                                    csv_row[k_col] = line_field[csv_head_known[k_col]]
                            except ValueError:
                                ...
                            record = Record()
                            if record.import_data(csv_row):
                                self.add_record(record)
                        result = True
            except FileNotFoundError:
                ...
        return result


    def __enter__(self):
        #print("__enter__")
        if self.auto_restore:
            self.import_csv()
        return self


    def __exit__(self, ext_type, ext_value, traceback):
        #print("__exit___")
        if self.auto_backup:
            self.export_csv()

    
    def __str__(self) -> str:
        result = [ str(i) for i in self.data.values() ]
        return "\n".join(result)


    def __iter__(self):
        self._page_pos = 0
        return self


    def __next__(self) -> list[Record]:
        if self._page_pos < len(self.data.keys()):
            result = []
            keys = list(self.data) \
                    [ self._page_pos:self._page_pos + self.max_records_per_page ]
            for key in keys:
                result.append(self.data[key])
            self._page_pos += self.max_records_per_page
            return result
        self._page_pos = 0
        raise StopIteration





