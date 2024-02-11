# Import the necessary libraries
from colorama import Fore
import sqlite3 as sql

# Establish a connection to the SQLite database file 'books.db'
# If the file does not exist, SQLite will create it
connection = sql.connect("books.db ")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Print a warning message in case of errors
print(Fore.RED + "\n!!! IF YOU GET AN ERROR AFTER THIS MESSAGE, PLEASE DELETE THE FILE 'books.db !!!!!!")

# Create a table named 'books' with columns 'title', 'author', and 'year'
createtable = "CREATE TABLE books (title TEXT, author TEXT, year INTEGER)"

# Execute the SQL command to create the table
cursor.execute(createtable)

# Insert data into the 'books' table
insert1 = "INSERT INTO books (title, author, year) values ('The Weirdstone of Brisingamen', 'Alan Garner',1960);"
insert2 = "INSERT INTO books (title, author, year) values ('Perdido Street Station','China Miéville',2000);"
insert3 = "INSERT INTO books (title, author, year) values ('Thud!','Terry Pratchett',2005);"
insert4 = "INSERT INTO books (title, author, year) values ('The Spellman Files','Lisa Lutz',2007);"
insert5 = "INSERT INTO books (title, author, year) values ('Small Gods','Terry Pratchett',1992);"

# Execute the SQL commands to insert the data
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)
cursor.execute(insert5)

# Print a success message
print(Fore.GREEN + "\nData inserted successfully!")

# Query the 'books' table to retrieve the titles of all books, ordered alphabetically by title
cursor.execute("SELECT title FROM books ORDER BY title")

# Fetch all the rows from the query result
output = cursor.fetchall()

# Print the titles of all the books
print(Fore.YELLOW + "\nBOOKS BY ALPHABETICAL ORDER\n" + Fore.RESET)
for title in output:
    print(title[0])

# Close the connection to the database
connection.close()