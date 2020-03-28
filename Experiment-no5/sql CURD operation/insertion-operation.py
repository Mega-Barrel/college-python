# This code is for adding data into a table.

import mysql.connector

def insertDataIntoTable(customer_id, customer_name, customer_address):
    
    mydb = mysql.connector.connect(host="localhost", user="root", passwd = "Saurabh240301", database = "customer")

    mycursor = mydb.cursor()

    mySql_insert_query = """INSERT INTO customer_information(customer_id, customer_name, customer_address) VALUES (%s, %s, %s)"""

    recordTuple = (customer_id, customer_name, customer_address)
    mycursor.execute(mySql_insert_query, recordTuple)

    mydb.commit()
    mycursor.close()
    mydb.close()
    # print('Data inserted successfully')

insertDataIntoTable(1, 'Saurabh', 'Vasai') # After update operation the address gets changed to borivali
insertDataIntoTable(2, 'Nilesh', 'Borivali')
insertDataIntoTable(3, 'Atharva', 'Andheri')
insertDataIntoTable(4, 'Chaitanya', 'Dadar')
insertDataIntoTable(5, 'Zack', 'Churchgate')
insertDataIntoTable(6, 'Sam', 'Bandra')

