import pymysql as mq

#server connection or database connection

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school")

mycursor = mysql.cursor()

# print("{:<13} {:20} {:20} {:<10}".format("Student Id", "Student Name", "Student Email","Student Class"))

# try:
#     sql = "SELECT * FROM student"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
    
#     for s in sdata:
#         print("{:<13} {:20} {:20} {:<10}".format(s[0],s[1],s[2],s[3]))
# except:
#     print("Error.....")



# <-- SELECT SPECIFIC COLUMN DATA -->


# print("{:<13} {:20}".format("Student Id", "Student Name"))

# try:
#     sql = "SELECT * FROM student"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
    
#     for s in sdata:
#         print("{:<13} {:20}".format(s[0],s[1]))
# except:
#     print("Error.....")



# <-- GET SINGLE ROW DATA -->

print("{:<13} {:20} {:20} {:<10}".format("Student Id", "Student Name", "Student Email","Student Class"))

try:
    sql = "SELECT * FROM student"
    mycursor.execute(sql)
    sdata = mycursor.fetchone()
    
    print("{:<13} {:20} {:20} {:<10}".format(sdata[0], sdata[1], sdata[2], sdata[3]))
except:
    print("Error.....")



# <-- GET SELECTION BASE DATA -->    



print("{:<13} {:20} {:20} {:<10}".format("Student Id", "Student Name", "Student Email","Student Class"))

try:
    sql = "SELECT * FROM student where st_id=3"
    mycursor.execute(sql)
    sdata = mycursor.fetchone()
    
    print("{:<13} {:20} {:20} {:<10}".format(sdata[0], sdata[1], sdata[2], sdata[3]))
except:
    print("Error.....")