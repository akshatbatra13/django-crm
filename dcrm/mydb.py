import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pass123'
)

# prepare a cursor object
cursorObject = db.cursor()

# create a database
cursorObject.execute("CREATE DATABASE mysqldb")
print("SUCCESS")
