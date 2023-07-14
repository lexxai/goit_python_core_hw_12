from chatbot.fields import Field, Name, Phone, Email, Address, Birthday
from datetime import date

class Record:

    def __init__(self, name: Name = None,
                 phone: Phone = None,
                 email: Email = None, 
                 address: Address = None, 
                 birthday: Birthday = None) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phones = []
        self.add_phone(phone)
        self.birthday = birthday


    def add(self, field: Field) -> bool:
        result = None
        if isinstance(field, Phone):
            result = self.add_phone(field)
        elif isinstance(field, Birthday):
            result = self.add_birthday(field)
        elif isinstance(field, Email):
            result = self.add_email(field)
        elif isinstance(field, Address):
            result = self.add_address(field)
        return result
            

    def add_phone(self, phone: Phone) -> None:
        if (phone):
            if (isinstance(phone, list)):
                for ph in phone:
                    if ph not in self.phones:
                        self.phones.append(ph)
                return True
            elif phone not in self.phones:
                self.phones.append(phone)
                return True


    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone and new_phone:
            for i, v in enumerate(self.phones):
                if self.phones[i] == old_phone:
                    self.phones[i] = new_phone
                    return True
    

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phones:
            self.phones.remove(phone)
            return True


    def get_phones(self) -> str:
        return ";".join([str(ph) for ph in self.phones])

    def filed_to_csv(self, value:str) -> str:
        """
            https://en.wikipedia.org/wiki/Comma-separated_values
        """
        if value.find(",") != -1:
            value = f'"{value}"'
        return value


    def _remove_None(self, string:str) -> str:
        return string.replace("None","")


    def get_csv_row(self) -> str:
        name = str(self.name)
        phone = self._remove_None(self.get_phones())
        email = self._remove_None(str(self.email))
        address = self._remove_None(self.filed_to_csv(str(self.address)))
        birthday=self._remove_None(str(self.birthday))
        row = f"{name},{phone},{email},{address},{birthday}"
        return row


    @staticmethod
    def get_csv_header() -> str:
        cols = ["name", "phone", "email", "address", "birthday"]
        return ",".join(cols)
    
    
    def import_data(self, data_row: dict):
        if data_row.get("name"):
            self.name = Name(data_row.get("name"))
            if data_row.get("phone"):
                self.add_phone(data_row.get("phone"))
            if data_row.get("email"):
                self.add_email(Email(data_row.get("email")))
            if data_row.get("address"):
                self.add_address(Address(data_row.get("address")))
            if data_row.get("birthday"):
                self.add_birthday(Birthday(data_row.get("birthday")))
            return True


    def add_birthday(self, birthday: Birthday) -> None:
        self.birthday = birthday
        return True


    def delete_birthday(self) -> None:
        if self.birthday:
            self.birthday = None
            return True


    def add_email(self, email: Email) -> None:
        self.email = email
        return True


    def delete_email(self) -> None:
        if self.email:
            self.email = None
            return True

    
    def add_address(self, address: Address) -> None:
        self.address = address
        return True


    def delete_address(self) -> None:
        if self.address:
            self.address = None
            return True


    def days_to_birthday(self) -> int:
        result = None
        if self.birthday:
            date_now = date.today()
            date_now_year = date_now.year
            bd = self.birthday.value.replace(year=date_now_year)
            if bd < date_now:
                date_now_year += 1
            bd = self.birthday.value.replace(year=date_now_year)
            diff_bd = bd - date_now
            result = diff_bd.days
        return result


    def __repr__(self):
        return str(self)
        

    def __str__(self) -> str:
        cols = [f"name: {self.name}"]
        if len(self.phones):
            cols.append(f"phones: {self.get_phones()}")
        if self.email:
            cols.append(f"email: {self.email}")
        if self.address:
            cols.append(f"address: {self.address}")
        if self.birthday:
            cols.append(f"birthday: {self.birthday}")
        return ", ".join(cols)
