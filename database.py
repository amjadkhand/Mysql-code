import pymysql as mq

# <-- Establishing the connection -->

mysql = mq.connect(
    host="localhost",
    user="root",
    password=""
)


# <-- CREATE  DATABASE -->

cursorobj = mysql.cursor()
try:

    db="create database school"
    cursorobj.execute(db)
    print("database created")
except:
    print("database error...")








