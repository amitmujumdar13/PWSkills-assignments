## Q1. What is a database? Differentiate between SQL and NoSQL databases.
## Answer: A database is an organized collection of structured information, or data, typically stored electronically in a computer system.
## SQL and NoSQL differ in whether they are relational (SQL) or non-relational (NoSQL), whether their schemas are predefined or dynamic, 
## how they scale, the type of data they include 
## and whether they are more fit for multi-row transactions or unstructured data.

## Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
## Answer: A database is an organized collection of structured information, or data, typically stored electronically in a computer system.
# SQL and NoSQL differ in whether they are relational (SQL) or non-relational (NoSQL), whether their schemas are predefined or dynamic, 
# how they scale, the type of data they include 
# and whether they are more fit for multi-row transactions or unstructured data.

# DDL is Data Definition language. CREATE is used to create a new table. 
# DROP will delete the table. ALTER will perform changes to columns of table or index changes.
# TRUNCATE will delete elements from table without deleting tables.
# Below are examples: 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="Amit"
)

mycursor = mydb.cursor()
## CREATE example
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
## ALTER TABLE 
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT")
## INSERT DATA 
mycursor.execute("INSERT INTO customers (id,name,address) values (1,'Amit','Pune')")
## Truncate TABLE 
mycursor.execute("TRUNCATE TABLE customers")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

## DROP TABLES
mycursor.execute("DROP TABLE customers")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)


## Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
##Answer :  DML is Data Manipulation language used to manipulate data in tables.
# Below are examples: 
## CREATE 
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
# INSERT will insert records into table
mycursor.execute("INSERT INTO customers (name,address) values ('Amit','Pune')")
# SELECT will get records from table
print("After Insert:")
mycursor.execute("SELECT name,address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# UPDATE will update row in table
mycursor.execute("UPDATE customers SET address='Mumbai' WHERE name='Amit'")
# SELECT will get records from table
print("After Update:")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# DELETE will update row in table
mycursor.execute("DELETE FROM customers WHERE name='Amit'")
# SELECT will get records from table
print("After DELETE:")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

## What is DQL? Explain SELECT with an example.
## Answer: DQL is Data Query language. It is used to fetch data from table.
# INSERT will insert records into table
mycursor.execute("INSERT INTO customers (name,address) values ('Amit','Pune')")
# SELECT will get records from table
print("After Insert:")
mycursor.execute("SELECT name,address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

## Q5. Explain Primary Key and Foreign Key.
# Answer: A relational database is designed to enforce the uniqueness of primary keys by allowing only one row with a given primary key value in a table. 
# A foreign key is a column or a set of columns in a table whose values correspond to the values of the primary key in another table.


## Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
import mysql.connector
mydb1 = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="Amit"
)

##A cursor keeps track of the position in the result set, and allows you to perform multiple operations row by row against a result set, with or without returning to the original table
mycursor1=mydb1.cursor()

## execute() method helps to run a query against tableusing cursor object.
mycursor1.execute("CREATE TABLE IF NOT EXISTS employee (name VARCHAR(20))")

## Q7. Give the order of execution of SQL clauses in an SQL query.

# Answer: 
# 1. FROM/JOIN: The FROM and/or JOIN clauses are executed first to determine the data of interest.
# 2. WHERE: The WHERE clause is executed to filter out records that do not meet the constraints.
# 3. GROUP BY: The GROUP BY clause is executed to group the data based on the values in one or more columns.
# 4. HAVING: The HAVING clause is executed to remove the created grouped records that don’t meet the constraints.
# 5. SELECT: The SELECT clause is executed to derive all desired columns and expressions.
# 6. ORDER BY: The ORDER BY clause is executed to sort the derived values in ascending or descending order.
# 7. LIMIT/OFFSET: Finally, the LIMIT and/or OFFSET clauses are executed to keep or skip a specified number of rows.