import mysql.connector

database = mysql.connector.connect(
    user="root",
    password="27_KdB_Mc",
    host="localhost",
    database="sedapal",
    port="3306"
)
print(database)