from chatbot.fields import Name, Phone, Birthday, Email, Address
from chatbot.record import Record
from functools import wraps


def parse_input(command_line: str) -> tuple[object, list]:
    line: str = command_line.lower().lstrip()
    for command, commands in COMMANDS.items():
        for command_str in commands:
            if len(line) > len(command_str):
                command_str += " "
            if line.startswith(command_str):
                args = command_line[len(command_str):].strip().split()
                args = [s.strip() for s in args]
                return command, args
    return handler_undefined, []


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
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
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            return result
        else:
            return "Done" if result else "The operation was not successful"
    return wrapper


@output_operation_describe
@input_error
def handler_add(*args, a_book) -> str:
    result = None
    user = args[0]
    args[1]
    phone = [Phone(p) for p in args[1:]]
    if user in a_book:
        result = a_book.get_record(user).add_phone(phone)
    else:
        rec = Record(Name(user), phone)
        result = a_book.add_record(rec)
    return result


@output_operation_describe
@input_error
def handler_change_phone(*args, a_book) -> str:
    user = args[0]
    old_phone = args[1]
    new_phone = args[2]
    return a_book.get_record(user).change_phone(Phone(old_phone), Phone(new_phone))


@output_operation_describe
@input_error
def handler_show_phone(*args, a_book) -> str:
    user = args[0]
    return a_book.get_record(user).get_phones()


@output_operation_describe
@input_error
def handler_delete_phone(*args, a_book) -> str:
    user = args[0]
    phone = args[1]
    return a_book.get_record(user).remove_phone(Phone(phone))


@output_operation_describe
@input_error
def handler_delete_record(*args, a_book) -> str:
    user = args[0]
    return a_book.remove_record(user)


@output_operation_describe
@input_error
def handler_delete_all_records(*args, a_book) -> str:
    if args[0] == "YES":
        return a_book.clear()


@output_operation_describe
def handler_show_all(*args, a_book) -> str:
    if a_book.len():
        return str(a_book)
    else:
        return "No users found, maybe you want to add them first?"


@input_error
def handler_show_page(*args, a_book) -> str:
    if args[0]:
        a_book.max_records_per_page = int(args[0])
    try:
        page = next(a_book)
        return "\n".join([str(i) for i in page])
    except StopIteration:
        return "End list"


def handler_show_csv(*args, a_book) -> str:
    if any(a_book.keys()):
        return a_book.get_csv()
    else:
        return "No users found, maybe you want to add them first?"


@output_operation_describe
@input_error
def handler_export_csv(*args, a_book) -> str:
    if len(args):
        filename = args[0]
    else:
        filename = None
    return (a_book.export_csv(filename))


@output_operation_describe
@input_error
def handler_import_csv(*args, a_book) -> str:
    if len(args):
        filename = args[0]
    else:
        filename = None
    return a_book.import_csv(filename)


def handler_hello(*args, a_book) -> str:
    return "How can I help you?"


def handler_help(*args, a_book) -> str:
    command = None
    if len(args):
        command = args[0]
    if not command:
        commands = sorted(list(c for cs in COMMANDS.values() for c in list(cs)))
        return "List of commands: " + ", ".join(commands)
    else:
        if type(command) == str:
            command = " ".join(args)
            command = get_command_handler(command)
        command_str: str = COMMANDS_HELP.get(command,
                                             "Help for this command is not yet available")
        if "{" in command_str:
            command_str = command_str.format(
                per_page=a_book.max_records_per_page,
                id_session=a_book.id
            )
        return command_str


@output_operation_describe
@input_error
def handler_add_birthday(*args, a_book) -> str:
    user = args[0]
    birthday = args[1]
    return a_book.get_record(user).add(Birthday(birthday))


@output_operation_describe
@input_error
def handler_add_email(*args, a_book) -> str:
    user = args[0]
    email = args[1]
    return a_book.get_record(user).add(Email(email))


@output_operation_describe
@input_error
def handler_add_address(*args, a_book) -> str:
    user = args[0]
    address = " ".join(args[1:])
    return a_book.get_record(user).add(Address(address))


@output_operation_describe
@input_error
def handler_delete_birthday(*args, a_book) -> str:
    user = args[0]
    return a_book.get_record(user).delete_birthday()


@output_operation_describe
@input_error
def handler_delete_email(*args, a_book) -> str:
    user = args[0]
    return a_book.get_record(user).delete_email()


@output_operation_describe
@input_error
def handler_delete_address(*args, a_book) -> str:
    user = args[0]
    return a_book.get_record(user).delete_address()


@output_operation_describe
@input_error
def handler_days_to_birthday(*args, a_book) -> str:
    user = args[0]
    result = a_book.get_record(user).days_to_birthday()
    if result is None:
        result = f"No birthday is defined for user: {user} "
    elif result == 0:
        result = f"{result} days, Today is user {user}'s birthday !!!"
    else:
        result = f"{result} days"
    return result


@output_operation_describe
@input_error
def handler_show_birthday(*args, a_book) -> str:
    user = args[0]
    result = a_book.get_record(user).birthday
    return result


@output_operation_describe
@input_error
def handler_show_email(*args, a_book) -> str:
    user = args[0]
    result = a_book.get_record(user).email
    return result


@output_operation_describe
@input_error
def handler_show_address(*args, a_book) -> str:
    user = args[0]
    result = a_book.get_record(user).address
    return result


def handler_exit(*args, a_book) -> str:
    return "Goodbye. We are looking forward to seeing you again."


def handler_undefined(*args, a_book) -> str:
    return handler_help(a_book=a_book)


def get_command_handler(command: str) -> object:
    for ch in COMMANDS:
        for cs in COMMANDS[ch]:
            if cs == command:
                return ch
    return handler_undefined


@output_operation_describe
@input_error
def handler_search(*args, a_book) -> str:
    pattern = args[0]
    result = a_book.search(pattern)
    return result


@input_error
def api(command: str, *args: list[str], a_book, verbose: bool = True) -> None:
    """API for run commands in batch mode

    Args:
        command (str): API command
        list[str]: API command arguments

    Returns:
        print API command result
    
    """
    result = get_command_handler(command)(*args, a_book=a_book)
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
    handler_delete_all_records: ("delete all records",),
    handler_change_phone: ("change phone", "="),
    handler_delete_phone: ("delete phone",),
    handler_show_phone: ("show phone",),
    handler_show_all: ("show all", "list", "l"),
    handler_show_page: ("show page",),
    handler_show_csv: ("show csv",),
    handler_export_csv: ("export csv", "e"),
    handler_import_csv: ("import csv", "i"),
    handler_help: ("help", "?"),
    handler_add_birthday: ("add birthday",),
    handler_delete_birthday: ("delete birthday",),
    handler_add_email: ("add email",),
    handler_delete_email: ("delete email",),
    handler_add_address: ("add address",),
    handler_delete_address: ("delete address",),
    handler_days_to_birthday:  ("to birthday", ),
    handler_show_birthday: ("show birthday",),
    handler_show_email: ("show email",),
    handler_show_address: ("show address",),
    handler_add: ("add", "+"),
    handler_search: ("search",),
    handler_exit: ("good bye", "close", "exit", "q", "quit")
}

"""
CONSTANT DICT OF COMMANDS HELP 
- key is pointer to handler function 
- value is help text for commands
"""
COMMANDS_HELP = {
    handler_hello: "Just hello",
    handler_delete_record: "Delete ALL records of user. Required username.",
    handler_delete_all_records: "Delete ALL records of ALL user. Required parameter YES",
    handler_change_phone: "Change user's phone. Required username, old phone, new phone",
    handler_delete_phone: "Delete user's phone. Required username, phone",
    handler_delete_email: "Delete user's email. Required username, email",
    handler_delete_address: "Delete user's address. Required username, address",
    handler_delete_birthday: "Delete user's birthday. Required username",
    handler_add_birthday: "Add or replace the user's birthday. Required username, birthday, "
                          "please use ISO 8601 date format",
    handler_add_email: "Add or replace the user's email. Required username, email",
    handler_add_address: "Add or replace the user's address. Required username, address",
    handler_show_phone: "Show user's phones. Required username.",
    handler_show_birthday: "Show user's birthday. Required username.",
    handler_show_email: "Show user's email. Required username.",
    handler_show_address: "Show user's address. Required username.",
    handler_show_all: "Show all user's record.",
    handler_show_page: "Show all user's record per page. Optional parameter size of page [{per_page}]",
    handler_show_csv: "Show all user's record in csv format",
    handler_export_csv: ("Export all user's record in csv format to file. Optional parameter filename",),
    handler_import_csv: ("Import all user's record in csv format to file. Optional parameter filename",),
    handler_days_to_birthday: "Show days until the user's birthday. Required username,",
    handler_add: "Add user's phone or multiple phones separated by space. "
                 "Required username and phone.",
    handler_help: "List of commands and their description. Also you can use '?' "
                  "for any command as parameter. Session ID: {id_session}",
    handler_exit: "Exit of bot.",
    handler_search: ("Search user by pattern in name or phone",),
    handler_undefined: "Help for this command is not yet available"
}
