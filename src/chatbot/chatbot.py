from chatbot.class_commands import Commands
from chatbot.address_book import AddressBook

# from chatbot.list_commands import parse_input,\
#     handler_help, handler_exit


class ChatBot(Commands):
    def __init__(self ,id: str = None,
                 auto_backup: bool = True,
                 auto_restore: bool = True,
                 init_callback=None):
        self.a_book = AddressBook(id=id,
                                  auto_backup=auto_backup,
                                  auto_restore=auto_restore)
        
        super().__init__(self.a_book)

        if init_callback:
            init_callback(self.a_book)


    def main(self):
        while True:
            try:
                user_input = input("Enter your command >>> ")
            except KeyboardInterrupt:
                print("\r")
                break

            command, args = self.parse_input(user_input)

            if len(args) == 1 and args[0] == "?":
                result = self.handler_help(command)
            else:
                result = command(self,*args)

            if result:
                print(result)

            if command == Commands.handler_exit:
                break
