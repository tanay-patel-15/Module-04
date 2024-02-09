import sqlite3 as sql

connection = sql.connect("inclass.db")

cursor = connection.cursor()

## run a bunch of queries

create_query = "CREATE TABLE IF NOT EXISTS People (personID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, town TEXT);"
cursor.execute(create_query)

insert_query_1 = "INSERT INTO People(name, age, town) VALUES(\"sally\", 34, \"sally\");"
insert_query_2 = "INSERT INTO People(name, age, town) VALUES(\"bob\", 56, \"new york city\");"
insert_query_3 = "INSERT INTO People(name, age, town) VALUES(\"daniel\", 68, \"sellersburg\");"

cursor.execute(insert_query_1)
cursor.execute(insert_query_2)
cursor.execute(insert_query_3)

select_query = "SELECT * from People WHERE age  > 50;"

cursor.execute(select_query)

data = cursor.fetchall()

for d in data:
  print(d[0], " is ", str(d[1]), " years old and lives in ", d[2], ".")



connection.close()