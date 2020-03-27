# Python code for connecting sql with python

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd = "Saurabh240301", database = "test")

mycursor = mydb.cursor()

mycursor.execute('select * from student1')

result = mycursor.fetchall()

print('Student Table data:')

for i in result:
    print(i)
