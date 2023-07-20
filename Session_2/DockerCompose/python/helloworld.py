import mysql.connector

connection = mysql.connector.connect(user="root",password="logesh",host="mysql", port="3306",database="db")
print("DB COnnected")
cur = connection.cursor()
cur.execute("select * from student")

std = cur.fetchall()

connection.close()

print(std)

 