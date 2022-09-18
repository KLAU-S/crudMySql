import mysql.connector as sql
connection = sql.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database="classicmodels"
)
# try: 
#     print(connection.connection_id)

# except:
#     print("connection was unsuccesfull")

