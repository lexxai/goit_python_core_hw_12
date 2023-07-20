import sys
sys.path.append('../src')
from chatbot import main as ChatBot
from chatbot.list_commands import api 



if __name__ == "__main__":

    def init(a_book):
        print("Pre init settings...")
        api("add", "Jon-00", "+38044333223", a_book=a_book)
        api("add birthday", "Jon-00", "1988-02-17", a_book=a_book)
        api("add", "Jon-01", "+38044333223", "33441", a_book=a_book)
        api("add", "Jon-02", "+38044333223", "33442", a_book=a_book)
        api("add", "Jon-03", "+38044333223", "33443", a_book=a_book)
        api("add", "Jon-04", "+38044333223", "33444", a_book=a_book)
        api("add", "Jon-05", "+38044333223", "33445", a_book=a_book)
        api("add", "Jon-06", "+38044333223", "33446", a_book=a_book)
        api("add", "Jon-07", "+38044333223", "33447", a_book=a_book)
        api("add", "Jon-08", "+38044333223", "33448", a_book=a_book)
        api("add", "Jon-09", "+38044333223", "33449", a_book=a_book)
        api("add", "Jon-10", "+38044333223", "33450", a_book=a_book)
        api("add", "Jon-11", "#38044333223", "33451", a_book=a_book)
        api("add", "Jon-12", "+38044333223", a_book=a_book)
        api("add email", "Jon-05", "jon05#example.com", a_book=a_book)
        api("add email", "Jon-02", "jon02@example.com", a_book=a_book)
        api("add address", "Jon-02",
                    "Vul. Vorota gate 02, office. 1221344", a_book=a_book)
        api("add address", "Jon-05",
                    "Vul. Vorota gate 112, office. 2332", a_book=a_book)
        api("add address", "Jon-07",
                    "Vul. Vorota gate 122", a_book=a_book)
        api("add birthday", "Jon-02", "1999-08-11", a_book=a_book)
        api("help", "add birthday", a_book=a_book)

    ChatBot.main(id="user-session-000001",
                  auto_backup=False,
                  auto_restore = False, 
                  init_callback = None)

