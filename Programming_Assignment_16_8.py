from colorama import Fore

import sqlite3 as sql

connection = sql.connect("books.db ")

cursor = connection.cursor()

print(Fore.RED + "\n!!! IF YOU GET AN ERROR AFTER THIS MESSAGE, PLEASE DELETE THE FILE 'books.db !!!!!!")

createtable = "CREATE TABLE books (title TEXT, author TEXT, year INTEGER)"

cursor.execute(createtable)

insert1 = "INSERT INTO books (title, author, year) values ('The Weirdstone of Brisingamen', 'Alan Garner',1960);"
insert2 = "INSERT INTO books (title, author, year) values ('Perdido Street Station','China Miéville',2000);"
insert3 = "INSERT INTO books (title, author, year) values ('Thud!','Terry Pratchett',2005);"
insert4 = "INSERT INTO books (title, author, year) values ('The Spellman Files','Lisa Lutz',2007);"
insert5 = "INSERT INTO books (title, author, year) values ('Small Gods','Terry Pratchett',1992);"

cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)
cursor.execute(insert5)

print(Fore.GREEN + "\nData inserted successfully!")

cursor.execute("SELECT title FROM books ORDER BY title")

output = cursor.fetchall()

print(Fore.YELLOW + "\nBOOKS BY ALPHABETICAL ORDER\n" + Fore.RESET)
for title in output:
    print(title[0])

print('\n')