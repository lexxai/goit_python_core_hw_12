# goit_python_core_hw_12

## v.0.5.0

moved to full use new classes:

- ChatBot child from Commands
- Commands

## v.0.4.6

- For class "address_book" was added methods for binary backup_data and restore_data by use module pickle.
- Main part added decorator for backup_data of selected handlers of commands
- added commands:
  - backup [version]
  - restore [version]
  - list versions
  - list csv

## v.0.4.5

- Tune alias list of commands on list of commands. For example: `show address ('?a'), show all ('list','l'), `
- Added filter of unknown commands in list of commands. For example:

```
Enter your command >>> show
List of commands: show address ('?a'), show all ('list','l'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show page ('?p'), show phone ('?p')
```

## v.0.4.4

- Split functions of commands to module list_commands.py
- Used external csv module for export import csv
- Added detection of commands only if there is a space after them, if they have parameters
- Added quoted parameters, like "Jon 11"
- Added a user session ID. It is used for hidden naming of csv files. Example: user-session-000001_chatboot_addresbook.csv
  - main(id: str = None
  - AddressBook(id: str = None,
- Added parameters to main / AddressBook
  - auto_backup: bool = True,
  - auto_restore: bool = True,
- Added parameter to class AddressBook
  - default_filename :str = "chatboot_addresbook",
- Added auto export / auto import on init / quit. Used filename with default name (chatboot_addresbook) and format csv
- Added parameter to main
  - init_callback = None, pointer to batch function on init
  - if init_callback used, then overwritten parameters: auto_backup = False, auto_restore = False,

### OUTPUT

```

ChatBot initialized...

Enter your command >>> l
name: Jon-00, phones: +38044333223, birthday: 1988-02-17
name: Jon-01, phones: +38044333223;33441
name: Jon-02, phones: +38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: +38044333223;33443
name: Jon-04, phones: +38044333223;33444
name: Jon-05, phones: +38044333223;33445, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: +38044333223;33446
name: Jon-07, phones: +38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: +38044333223;33448
name: Jon-09, phones: +38044333223;33449
name: Jon-10, phones: +38044333223;33450
name: Jon-12, phones: +38044333223
Enter your command >>> clear
List of commands: +, -, ?, add, add address, add birthday, add email, change phone, close, delete address, delete all records, delete birthday, delete email, delete phone, delete user, e, exit, export csv, good bye, hello, help, i, import csv, l, list, q, quit, search, show address, show all, show birthday, show csv, show email, show page, show phone, to birthday
Enter your command >>> delete all records ?
Delete ALL records of ALL user. Required parameter YES
Enter your command >>> delete all records yES
The operation was not successful
Enter your command >>> delete all records YES
Done
Enter your command >>> l
No users found, maybe you want to add them first?
Enter your command >>> import csv
Done
Enter your command >>> l
name: Jon-00, phones: +38044333223, birthday: 1988-02-17
name: Jon-01, phones: +38044333223;33441
name: Jon-02, phones: +38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: +38044333223;33443
name: Jon-04, phones: +38044333223;33444
name: Jon-05, phones: +38044333223;33445, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: +38044333223;33446
name: Jon-07, phones: +38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: +38044333223;33448
name: Jon-09, phones: +38044333223;33449
name: Jon-10, phones: +38044333223;33450
name: Jon-12, phones: +38044333223
Enter your command >>> serarch -06
List of commands: +, -, ?, add, add address, add birthday, add email, change phone, close, delete address, delete all records, delete birthday, delete email, delete phone, delete user, e, exit, export csv, good bye, hello, help, i, import csv, l, list, q, quit, search, show address, show all, show birthday, show csv, show email, show page, show phone, to birthday
Enter your command >>> search -06
name: Jon-06, phones: +38044333223;33446
Enter your command >>> search -1
name: Jon-10, phones: +38044333223;33450
name: Jon-12, phones: +38044333223
Enter your command >>> search 444
name: Jon-04, phones: +38044333223;33444
Enter your command >>> search 44
name: Jon-00, phones: +38044333223, birthday: 1988-02-17
name: Jon-01, phones: +38044333223;33441
name: Jon-02, phones: +38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: +38044333223;33443
name: Jon-04, phones: +38044333223;33444
name: Jon-05, phones: +38044333223;33445, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: +38044333223;33446
name: Jon-07, phones: +38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: +38044333223;33448
name: Jon-09, phones: +38044333223;33449
name: Jon-10, phones: +38044333223;33450
name: Jon-12, phones: +38044333223
Enter your command >>> export csv
saved to filename : chatboot_addresbook.csv
Enter your command >>> export csv one.csv
saved to filename : one.csv
Enter your command >>> delete all records YES
Done
Enter your command >>> l
No users found, maybe you want to add them first?
Enter your command >>> import one.csv
List of commands: +, -, ?, add, add address, add birthday, add email, change phone, close, delete address, delete all records, delete birthday, delete email, delete phone, delete user, e, exit, export csv, good bye, hello, help, i, import csv, l, list, q, quit, search, show address, show all, show birthday, show csv, show email, show page, show phone, to birthday
Enter your command >>> import csv one.csv
Done
Enter your command >>> list
name: Jon-00, phones: +38044333223, birthday: 1988-02-17
name: Jon-01, phones: +38044333223;33441
name: Jon-02, phones: +38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: +38044333223;33443
name: Jon-04, phones: +38044333223;33444
name: Jon-05, phones: +38044333223;33445, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: +38044333223;33446
name: Jon-07, phones: +38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: +38044333223;33448
name: Jon-09, phones: +38044333223;33449
name: Jon-10, phones: +38044333223;33450
name: Jon-12, phones: +38044333223
Enter your command >>> show cv
List of commands: +, -, ?, add, add address, add birthday, add email, change phone, close, delete address, delete all records, delete birthday, delete email, delete phone, delete user, e, exit, export csv, good bye, hello, help, i, import csv, l, list, q, quit, search, show address, show all, show birthday, show csv, show email, show page, show phone, to birthday
Enter your command >>> show csv
name,phone,email,address,birthday
Jon-00,+38044333223,,,1988-02-17
Jon-01,+38044333223;33441,,,
Jon-02,+38044333223;33442,jon02@example.com,"Vul. Vorota gate 02, office. 1221344",1999-08-11
Jon-03,+38044333223;33443,,,
Jon-04,+38044333223;33444,,,
Jon-05,+38044333223;33445,,"Vul. Vorota gate 112, office. 2332",
Jon-06,+38044333223;33446,,,
Jon-07,+38044333223;33447,,Vul. Vorota gate 122,
Jon-08,+38044333223;33448,,,
Jon-09,+38044333223;33449,,,
Jon-10,+38044333223;33450,,,
Jon-12,+38044333223,,,
Enter your command >>> export csv
Exported successfully to "chatboot_addresbook.csv" file
Enter your command >>> export csv one.csv
Exported successfully to "one.csv" file
Enter your command >>> import csv
Done
import csv one.csv
Done
Enter your command >>> show
List of commands: show address ('?a'), show all ('list','l'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show page ('?p'), show phone ('?p')
Enter your command >>> delete
List of commands: delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-')
Enter your command >>> ?
List of commands: add ('+'), add address ('+a'), add birthday ('+b'), add email ('+e'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i'), search ('?='), show address ('?a'), show all ('list','l'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show page ('?p'), show phone ('?p'), to birthday ('2b')
Enter your command >>> ch
List of commands: change phone ('=p')
Enter your command >>> ad
List of commands: add ('+'), add address ('+a'), add birthday ('+b'), add email ('+e')
Enter your command >>> ? q
Exit of bot.
Enter your command >>> q
Goodbye. We are looking forward to seeing you again.
```

## backup / restore v.0.4.6

```
Initializing a ChatBot...

Enter your command >>> ?
List of commands: add ('+'), add address ('+a'), add birthday ('+b'), add email ('+e'), backup ('bak'), change phone ('=p'), delete address ('-a'), delete all records ('---'), delete birthday ('-b'), delete email ('-e'), delete phone ('-p'), delete user ('-'), export csv ('e'), good bye ('close','exit','q','quit'), hello, help ('?'), import csv ('i'), list csv ('lcsv'), list versions ('lv'), restore ('res'), search ('?='), show address ('?a'), show all ('list','l'), show birthday ('?b'), show csv ('?csv'), show email ('?e'), show page ('?p'), show phone ('?p'), to birthday ('2b')
Enter your command >>> list
No users found, maybe you want to add them first?
Enter your command >>> restore
Done
Enter your command >>> list
No users found, maybe you want to add them first?
Enter your command >>> list versions
Done
Enter your command >>> list csv ?
List of saved cvs files
Enter your command >>> list csv
aa.csv
chatboot_addresbook.csv
one.csv
Enter your command >>> import csv ?
Import all user's record in csv format to file. Optional parameter filename
Enter your command >>> import csv chatboot_addresbook.csv
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Jon 12, phones: +38044333223
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: Jon 17, phones: 32323243434;11;11111;2222, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w, fdfefff    e, birthday: 1999-09-09
name: www, phones: 2222
Enter your command >>> backup
Done
Enter your command >>> backup 1
Done
Enter your command >>> - "Jon 17"
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Jon 12, phones: +38044333223
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
Enter your command >>> - "Jon 12"
Done
Enter your command >>> l
name: Jon-10, phones: +38044333223;33450
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
Enter your command >>> backup 1
Done
Enter your command >>> add Ostap 1232333
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
name: Ostap, phones: 1232333
Enter your command >>> backup 2
Done
Enter your command >>> list versions
version: 1
version: 2
Enter your command >>> --- ?
Delete ALL records of ALL user. Required parameter YES
Enter your command >>> --- YES
Done
Enter your command >>> list
No users found, maybe you want to add them first?
Enter your command >>> restore ?
Restore all records. Optional parameter is the version.
Enter your command >>> restore 2
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
name: Ostap, phones: 1232333
Enter your command >>> restore 1
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
Enter your command >>> restore
Done
Enter your command >>> list
No users found, maybe you want to add them first?
Enter your command >>> restore 2
Done
Enter your command >>> list
name: Jon-10, phones: +38044333223;33450
name: Abrams, phones: 999, address: dsdsd dwd wdwd wd wdw wd wdwdwdw wd w
name: www, phones: 2222
name: Ostap, phones: 1232333
Enter your command >>>
```
