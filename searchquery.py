import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school")

mycursor = mysql.cursor()

print("{:<13} {:20} {:20}".format("Student Id", "Student Name", "Student Class "))


# try:
#     name = input("Enter the Student Name:- ")
#     sql = "SELECT * from student where st_name= '"+name+"' "
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()

#     for s in sdata:
#         print("{:<13} {:20} {:20}".format(s[0], s[1], s[2], s[3]))
# except:
#     print("Error....")


# <-- Use like % operatror for searching -->    

# try:
#     name = input("Enter the Student Name:- ")
#     sql = "SELECT * from student where st_name like '%"+name+"%' "
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()

#     for s in sdata:
#         print("{:<13} {:20} {:20}".format(s[0], s[1], s[2], s[3]))
# except:
#     print("Error....")


# <-- search with two fields like % operatror for searching -->    

try:
    name = input("Enter the Student Name:- ")
    classname = input("Enter the Student Class Name:- ")
    # sql = "SELECT * from student where st_name like '%"+name+"%' and st_class= '"+classname+"' "
    sql = "SELECT * from student where st_name like '%"+name+"%' or st_class= '"+classname+"' "
 
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<13} {:20} {:20}".format(s[0], s[1], s[2], s[3]))
except:
    print("Error....")    