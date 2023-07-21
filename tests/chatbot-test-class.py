import sys
sys.path.append('../src')
from chatbot.chatbot import ChatBot
#from chatbot.list_commands import api 

def init_chat(chat):
    print("Pre init settings...", chat)
    chat.api("add", "Jon-00", "+38044333223")
    chat.api("add birthday", "Jon-00", "1988-02-17")
    chat.api("add", "Jon-01", "+38044333223", "33441")
    chat.api("add", "Jon-02", "+38044333223", "33442")
    chat.api("add", "Jon-03", "+38044333223", "33443")
    chat.api("add", "Jon-04", "+38044333223", "33444")
    chat.api("add", "Jon-05", "+38044333223", "33445")
    chat.api("add", "Jon-06", "+38044333223", "33446")
    chat.api("add", "Jon-07", "+38044333223", "33447")
    chat.api("add", "Jon-08", "+38044333223", "33448")
    chat.api("add", "Jon-09", "+38044333223", "33449")
    chat.api("add", "Jon-10", "+38044333223", "33450")
    chat.api("add", "Jon-11", "#38044333223", "33451")
    chat.api("add", "Jon-12", "+38044333223")
    chat.api("add email", "Jon-05", "jon05#example.com")
    chat.api("add email", "Jon-02", "jon02@example.com")
    chat.api("add address", "Jon-02",
                "Vul. Vorota gate 02, office. 1221344")
    chat.api("add address", "Jon-05",
                "Vul. Vorota gate 112, office. 2332")
    chat.api("add address", "Jon-07",
                "Vul. Vorota gate 122")
    chat.api("add birthday", "Jon-02", "1999-08-11")
    chat.api("help", "add birthday")

if __name__ == "__main__":
    chats = []
    session = "user-session-000001"
    chat = ChatBot(id=session,
                    auto_backup=True,
                    auto_restore=True, init_callback=None)
    chats.append(chat)
    for c in chats:
        print(f"Session: {c.id_session}")
    #init_chat(chat)
    if False:
        verbose = False
        chat.api("add", "Jon-00", "+38044333223", "+38044333221", verbose=verbose)
        chat.api("add email", "Jon-00", "jon05@example.com", verbose=verbose)
        chat.api("add address", "Jon-00",
                "вул. Ворота Гетьмана, буд. 02, офіс. 121-344", verbose=verbose)
        chat.api("add birthday", "Jon-00", "1999-08-11", verbose=verbose)
        chat.api("help", "add birthday", verbose=verbose)
    chat.main()



