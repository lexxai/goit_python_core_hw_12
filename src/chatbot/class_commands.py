from chatbot.fields import Name, Phone, Birthday, Email, Address
from chatbot.record import Record
from functools import wraps


class Commands:

    def __init__(self, a_book):
        self.a_book = a_book

    def split_line_by_space(self, line: str) -> list[str]:
        """ split_line_by_space with quotes

        Args:
            line (str): "Jon 12" +32323243434 33033440

        Returns:
            list: ["Jon 12", "+32323243434", "33033440"]
        """
        parts = []
        current_part = ''
        inside_quotes = False
        for char in line:
            if char == ' ' and not inside_quotes:
                parts.append(current_part.strip())
                current_part = ''
            elif char == '"':
                inside_quotes = not inside_quotes
            else:
                current_part += char
        parts.append(current_part.strip())
        return list(filter(lambda x: x, parts))


    def parse_input(self, command_line: str) -> tuple[object, list]:
        line: str = command_line.lower().lstrip()
        for command, commands in self.COMMANDS.items():
            for command_str in commands:
                if len(line) > len(command_str):
                    command_str += " "
                if line.startswith(command_str):
                    #args = command_line[len(command_str):].strip().split()
                    args = self.split_line_by_space(
                        command_line[len(command_str):].strip())
                    return command, args
        return Commands.handler_undefined, [line]


    def backup_data(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.a_book.backup_data()
            return result
        return wrapper

        
    def input_error(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except (KeyError, ValueError, IndexError) as e:
                error = str(e)
                return f"Sorry, there are not enough parameters or their value may be incorrect {error}. "\
                    "Please use the help for more information. "
            except (FileNotFoundError):
                return "Sorry, there operation with file is incorrect."
            except Exception as e:
                return "**** Exception other: " + str(e)
        return wrapper


    def output_operation_describe(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if type(result) == str:
                return result
            else:
                return "Done" if result else "The operation was not successful"
        return wrapper


    @output_operation_describe
    @backup_data
    @input_error
    def handler_add(self, *args) -> str:
        result = None
        user = args[0]
        args[1]
        phone = [Phone(p) for p in args[1:]]
        if user in self.a_book:
            result = self.a_book.get_record(user).add_phone(phone)
        else:
            rec = Record(Name(user), phone)
            result = self.a_book.add_record(rec)
        return result


    @output_operation_describe
    @backup_data
    @input_error
    def handler_change_phone(self, *args) -> str:
        user = args[0]
        old_phone = args[1]
        new_phone = args[2]
        return self.a_book.get_record(user).change_phone(Phone(old_phone), Phone(new_phone))


    @output_operation_describe
    @input_error
    def handler_show_phone(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).get_phones()


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_phone(self, *args) -> str:
        user = args[0]
        phone = args[1]
        return self.a_book.get_record(user).remove_phone(Phone(phone))


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_record(self, *args) -> str:
        user = args[0]
        return self.a_book.remove_record(user)


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_all_records(self, *args) -> str:
        if args[0] == "YES":
            return self.a_book.clear()


    @output_operation_describe
    def handler_show_all(self, *args) -> str:
        if self.a_book.len():
            return str(self.a_book)
        else:
            return "No users found, maybe you want to add them first?"


    @input_error
    def handler_show_page(self, *args) -> str:
        if args[0]:
            self.a_book.max_records_per_page = int(args[0])
        try:
            page = next(self.a_book)
            return "\n".join([str(i) for i in page])
        except StopIteration:
            return "End list"


    def handler_show_csv(self, *args) -> str:
        if any(self.a_book.keys()):
            return self.a_book.get_csv()
        else:
            return "No users found, maybe you want to add them first?"


    @output_operation_describe
    @input_error
    def handler_export_csv(self, *args) -> str:
        if len(args):
            filename = args[0]
        else:
            filename = None
        return (self.a_book.export_csv(filename))


    @output_operation_describe
    @input_error
    def handler_import_csv(self, *args) -> str:
        if len(args):
            filename = args[0]
        else:
            filename = None
        return self.a_book.import_csv(filename)


    def handler_hello(self, *args) -> str:
        return "How can I help you?"


    def handler_help(self, *args, help_filter=None) -> str:
        command = None
        if len(args):
            command = args[0]
        if not command:
            commands = []
            for cs in self.COMMANDS.values():
                if help_filter and not any(
                    filter(lambda x: x.startswith(help_filter), cs)
                    ):
                    continue
                c_str = ""
                c_alias = []
                for c in list(cs):
                    if len(c_str) == 0:
                        c_str = c
                    else:
                        c_alias.append(f"'{c}'")
                c_alias_str = ",".join(c_alias)
                if any(c_alias):
                    c_str += f" ({c_alias_str})"
                commands.append(c_str)
            #commands = sorted(list(c for cs in self.COMMANDS.values() for c in list(cs)))
            return "List of commands: " + ", ".join(sorted(commands))
        else:
            if type(command) == str:
                command = " ".join(args)
                command = get_command_handler(command)
            command_str: str = self.COMMANDS_HELP.get(command,
                                                "Help for this command is not yet available")
            if "{" in command_str:
                command_str = command_str.format(
                    per_page=self.a_book.max_records_per_page,
                    id_session=self.a_book.id
                )
            return command_str


    @output_operation_describe
    @backup_data
    @input_error
    def handler_add_birthday(self, *args) -> str:
        user = args[0]
        birthday = args[1]
        return self.a_book.get_record(user).add(Birthday(birthday))


    @output_operation_describe
    @backup_data
    @input_error
    def handler_add_email(self, *args) -> str:
        user = args[0]
        email = args[1]
        return self.a_book.get_record(user).add(Email(email))


    @output_operation_describe
    @backup_data
    @input_error
    def handler_add_address(self, *args) -> str:
        user = args[0]
        address = " ".join(args[1:])
        return self.a_book.get_record(user).add(Address(address))


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_birthday(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_birthday()


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_email(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_email()


    @output_operation_describe
    @backup_data
    @input_error
    def handler_delete_address(self, *args) -> str:
        user = args[0]
        return self.a_book.get_record(user).delete_address()


    @output_operation_describe
    @input_error
    def handler_days_to_birthday(self, *args) -> str:
        user = args[0]
        result = self.a_book.get_record(user).days_to_birthday()
        if result is None:
            result = f"No birthday is defined for user: {user} "
        elif result == 0:
            result = f"{result} days, Today is user {user}'s birthday !!!"
        else:
            result = f"{result} days"
        return result


    @output_operation_describe
    @input_error
    def handler_show_birthday(self, *args) -> str:
        user = args[0]
        result = str(self.a_book.get_record(user).birthday)
        return result


    @output_operation_describe
    @input_error
    def handler_show_email(self, *args) -> str:
        user = args[0]
        result = self.a_book.get_record(user).email
        return result


    @output_operation_describe
    @input_error
    def handler_show_address(self, *args) -> str:
        user = args[0]
        result = self.a_book.get_record(user).address
        return result


    def handler_exit(self, *args) -> str:
        return "Goodbye. We are looking forward to seeing you again."


    def handler_undefined(self, *args) -> str:
        command = None
        if any(args):
            command = args[0]
        return self.handler_help(help_filter=command)


    def get_command_handler(command: str) -> object:
        for ch in self.COMMANDS:
            for cs in self.COMMANDS[ch]:
                if cs == command:
                    return ch
        return self.handler_undefined


    @output_operation_describe
    @input_error
    def handler_search(self, *args) -> str:
        pattern = args[0]
        result = self.a_book.search(pattern)
        return result


    @output_operation_describe
    def handler_backup(self, *args) -> bool:
        version = None
        if any(args):
            version = args[0]
        result = self.a_book.backup_data(version)
        return result


    @output_operation_describe
    def handler_restore(self, *args) -> bool:
        version = None
        if any(args):
            version = args[0]
        result = self.a_book.restore_data(version)
        return result


    @output_operation_describe
    def handler_list_versions(self, *args) -> str:
        result = self.a_book.list_versions()
        return result
        

    @output_operation_describe
    def handler_list_csv(self, *args) -> str:
        result = self.a_book.list_csv()
        return result    
        

    @input_error
    def api(self, command: str, *args: list[str], verbose: bool = True) -> None:
        """API for run commands in batch mode

        Args:
            command (str): API command
            list[str]: API command arguments

        Returns:
            print API command result
        
        """
        result = self.get_command_handler(command)(*args)
        if verbose:
            print(f"api command '{command}': {result}")
        else:
            return result

    """
    CONSTANT DICT OF COMMANDS LIST 
    - key is pointer to handler function 
    - value is list of chat bot commands
    """
    COMMANDS = {
        handler_hello: ("hello",),
        handler_delete_record: ("delete user", "-"),
        handler_delete_all_records: ("delete all records","---"),
        handler_change_phone: ("change phone", "=p"),
        handler_delete_phone: ("delete phone","-p"),
        handler_show_phone: ("show phone","?p"),
        handler_show_page: ("show page","?p"),
        handler_show_csv: ("show csv","?csv"),
        handler_export_csv: ("export csv", "e"),
        handler_import_csv: ("import csv", "i"),
        handler_help: ("help", "?"),
        handler_add_birthday: ("add birthday","+b"),
        handler_delete_birthday: ("delete birthday","-b"),
        handler_add_email: ("add email","+e"),
        handler_delete_email: ("delete email","-e"),
        handler_add_address: ("add address","+a"),
        handler_delete_address: ("delete address","-a"),
        handler_days_to_birthday:  ("to birthday", "2b"),
        handler_show_birthday: ("show birthday","?b"),
        handler_show_email: ("show email","?e"),
        handler_show_address: ("show address","?a"),
        handler_backup: ("backup", "bak"),
        handler_restore: ("restore", "res"),
        handler_list_versions: ("list versions", "lv"),    
        handler_list_csv: ("list csv", "lcsv"),     
        handler_show_all: ("show all", "list", "l"),
        handler_add: ("add", "+"),
        handler_search: ("search","?="),
        handler_exit: ("good bye", "close", "exit", "q", "quit"),
    }

    """
    CONSTANT DICT OF COMMANDS HELP 
    - key is pointer to handler function 
    - value is help text for commands
    """
    COMMANDS_HELP = {
        handler_hello: "Just hello",
        handler_delete_record: "Delete ALL records of user. Required username.",
        handler_delete_all_records: "Delete ALL records of ALL user. "
                                          "Required parameter YES",
        handler_change_phone: "Change user's phone. "
                                   "Required username, old phone, new phone",
        handler_delete_phone: "Delete user's phone. Required username, phone",
        handler_delete_email: "Delete user's email. Required username, email",
        handler_delete_address: "Delete user's address. "
                                     "Required username, address",
        handler_delete_birthday: "Delete user's birthday. Required username",
        handler_add_birthday: "Add or replace the user's birthday. "
                                   "Required username, birthday, "
                            "please use ISO 8601 date format",
        handler_add_email: "Add or replace the user's email. "
                                "Required username, email",
        handler_add_address: "Add or replace the user's address. "
                                  "Required username, address",
        handler_show_phone: "Show user's phones. Required username.",
        handler_show_birthday: "Show user's birthday. Required username.",
        handler_show_email: "Show user's email. Required username.",
        handler_show_address: "Show user's address. Required username.",
        handler_show_all: "Show all user's record.",
        handler_show_page: "Show all user's record per page. "
                                "Optional parameter size of page [{per_page}]",
        handler_show_csv: "Show all user's record in csv format",
        handler_export_csv: "Export all user's record in csv format to file. "
                                 "Optional parameter filename",
        handler_import_csv: "Import all user's record in csv format to file. "
                                 "Optional parameter filename",
        handler_days_to_birthday: "Show days until the user's birthday. "
                                       "Required username,",
        handler_add: "Add user's phone or multiple phones separated by space. "
                    "Required username and phone.",
        handler_help: "List of commands and their description. "
                            "Also you can use '?' "
                            "for any command as parameter. Session ID: {id_session}",
        handler_exit: "Exit of bot.",
        handler_search: "Search user by pattern in name or phone",
        handler_backup: "Backup all records. Optional parameter is the version. "
                        "P.S. it done automatically after any changes on records",
        handler_restore: "Restore all records. Optional parameter is the version.",
        handler_list_versions: "List of saved backup versions",
        handler_list_csv: "List of saved cvs files",
        handler_undefined: "Help for this command is not yet available"
    }
