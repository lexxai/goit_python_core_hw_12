from chatbot.address_book import AddressBook
from chatbot.list_commands  import parse_input,\
            handler_help, handler_exit


def main(id: str = None, 
         auto_backup: bool = True, 
         auto_restore: bool = True, 
         init_callback = None):

    print("\nChatBot initialized...\n")

    if init_callback:
            auto_backup = False
            auto_restore = False

    with AddressBook(id = id, 
                     auto_backup = auto_backup, 
                     auto_restore = auto_restore) as a_book:

        if init_callback:
            init_callback(a_book)

        while True:
            try:
                user_input = input("Enter your command >>> ")
            except KeyboardInterrupt:
                print("\r")
                break
            
            command, args = parse_input(user_input)
            
            if len(args) == 1 and  args[0] == "?" :
                result = handler_help(command, a_book=a_book)
            else:
                result = command(*args, a_book=a_book)
            
            if result:
                    print(result)

            if command == handler_exit:
                break


if __name__ == "__main__":
    main()

