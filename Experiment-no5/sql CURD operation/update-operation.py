# This code is for updating data in sql

import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'Saurabh240301', database = 'customer')

mycursor = mydb.cursor()

sql = "UPDATE customer_information SET customer_address = 'Borivali' where customer_name = 'saurabh'"

mycursor.execute(sql)

mydb.commit()
mycursor.close()
mydb.close()

print(mycursor.rowcount, 'rows affected')
