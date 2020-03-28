import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'Saurabh240301', database = 'customer')

mycursor = mydb.cursor()

sql = "DELETE FROM customer_information WHERE customer_name = 'Nilesh'"

mycursor.execute(sql)

mydb.commit()
mycursor.close()
mydb.close()

print(mycursor.rowcount, 'rows affected')

