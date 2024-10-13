import pymysql as mq

mysql = mq.connect(
      host="localhost",
    user="root",
    password="",
    database = "ecomerce"
)

mycursor = mysql.cursor()


# print("{:<15} {:<15} {:<15}".format("EMP No","EMP Name", "EMP DName"))

# try:
#     sql = "SELECT empno, empname,deptname from employee"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall() 
#     for s in sdata:
#         print("{:<15} {:<15} {:<15}".format(s[0], s[1],s[2]))
# except:
#     print("Error...")



 # <-- PERFORMS OPERATIONS DISTNICT -->    


print("{:<15}".format("EMP DName"))
try:
    sql = "SELECT distinct deptname from employee"
    mycursor.execute(sql)
    sdata = mycursor.fetchall() 
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error...")