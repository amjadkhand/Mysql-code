import pymysql as mq


# <-- Establishing the connection -->

# mysql = mq.connect(
#     host="localhost",
#     user="root",
#     password=""
#  )


# <-- CREATE  DATABASE -->



# mycursor = mysql.cursor()

# try:
#     db = "create database ecomerce" 
#     mycursor.execute(db)
#     print("Database created")

# except:
#     print("database error....")



# <-- CREATE TABLE IN  DATABASE -->

# mysql = mq.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "",
#     database = "ecomerce" 
# )

# mycursor = mysql.cursor()

# tc = '''CREATE TABLE categories (
#     cat_id INT PRIMARY KEY AUTO_INCREMENT,
#     cat_name VARCHAR(50),
#     prent_id INTEGER
   
# );'''

# mycursor.execute(tc)
# mysql.commit()  # Don't forget to commit the transaction



# <-- INSET RECORD IN TABLE  ECOMERCE -->



mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ecomerce" 
)

mycursor = mysql.cursor()

try:
    ins= "INSERT INTO categories (cat_name,prent_id ) values ('Jewellery',2)"
    mycursor.execute(ins)
    mysql.commit()
    print("Insert Data ")
    
except:
    print('Error...')

