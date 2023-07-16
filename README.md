# goit_python_core_hw_12

## v.0.4.4

Split functions of commands to module list_commands.py
Used external csv module for export import csv
Added quoted parameters, like "Jon 11"
Added user session id. Used on hidden file name of csv files.

- main(id: str = None
- AddressBook(id: str = None,

Added parameters to main / AddressBook

- auto_backup
- auto_restores

Added parameter to main

- init_callback = None, pointer to batch function on init

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
Enter your command >>> q
```
