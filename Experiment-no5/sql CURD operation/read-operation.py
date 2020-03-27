# Read operation is done wite select statement.

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd = "Saurabh240301", database = "customer")

mycursor = mydb.cursor()

mycursor.execute('select * from customer_information')

result = mycursor.fetchall()

print('Printing Student Table data:\n')

for i in result:
    print("customer_id = ", i[0])
    print("customer_name = ", i[1])
    print("customer_address  = ", i[2], '\n')
    
mydb.close()
mycursor.close()