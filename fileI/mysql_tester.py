import mysql.connector

myconnection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "ikku"
)
cursor = myconnection.cursor()
# cursor.execute("SHOW DATABASES")
cursor.execute("select * from student")

if myconnection.is_connected():
    print("yes")

