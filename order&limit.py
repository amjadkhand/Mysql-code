import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school")

mycursor = mysql.cursor()

print("{:<13} {:20} {:20}".format("Student Id", "Student Name", "Student Class "))


# try:
#     # asc, desc
#     sql = "SELECT * FROM student order by st_name desc"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()

#     for s in sdata:
#          print("{:<13} {:20} {:20}".format(s[0], s[1], s[2]))
# except:
#     print("Error....")


# <-- Use limit order by-->    


try:
    # asc, desc
    sql = "SELECT * FROM student order by st_id desc limit 2,3"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
         print("{:<13} {:20} {:20}".format(s[0], s[1], s[2]))
except:
    print("Error....")