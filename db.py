import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SynysterGates1',
    database='horus'
)

cursor = database.cursor()