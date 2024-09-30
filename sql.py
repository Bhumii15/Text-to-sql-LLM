import sqlite3

#connect to sqlite
connection = sqlite3.connect("stu.db")

#create a cursor object to insert record,create table,retrive

cursor = connection.cursor()

#create table
table_info = """
Create table New_Student(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT,ADDRESS VARCHAR(50));
"""
cursor.execute(table_info)

#insert some records
cursor.execute('''Insert Into New_Student values('abc','Data Science','A',99,'Gujarat')''')
cursor.execute('''Insert Into New_Student values('def','Data Analyst','B',89,'Gujarat')''')
cursor.execute('''Insert Into New_Student values('ghi','Data Science','A',90,'Maharashtra')''')
cursor.execute('''Insert Into New_Student values('jkl','Data Engineer','A',79,'Gujarat')''')
cursor.execute('''Insert Into New_Student values('mno','Data Science','B',96,'Maharashtra')''')

#display all records
print("The inserted records are")

data = cursor.execute(''' Select * From New_Student''')

for row in data:
    print(row)

#close the connection

connection.commit()
connection.close() 