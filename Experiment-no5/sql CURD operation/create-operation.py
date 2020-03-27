# Write a python program to implement CURD operation in sql.

'''
CURD stand for 
1. Create
2. Update
3. Read
4. Delete
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd = "Saurabh240301", database = "customer")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer_information(customer_id INT, customer_name VARCHAR(50), customer_address VARCHAR(50))")

mydb.commit()

