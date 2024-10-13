import pymysql as mq

# <-- CREATE TABLE -->

mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ecomerce" 
)

mycursor = mysql.cursor() 

# tc = '''CREATE TABLE employee (
#     empno INTEGER,
#     empname varchar(50),
#     deptname varchar(100)
# );'''

# mycursor.execute(tc)
# mysql.commit()



# <-- INSERT RECORD IN TABLE -->


# ins= "INSERT INTO employee (empno,empname, deptname) values (3,'WARD','SALESMAN')"
# mycursor.execute(ins)
# mysql.commit()
# print("Insert Data ")



# <-- PERFORMS OPERATIONS -->

# print("{:<15}".format("EMP NAME"))

# try:
#     sql = "SELECT deptname from employee"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
#     for s in sdata:
#         print("{:<15}".format(s[0]))
# except:
#     print("Error...")



    # <-- PERFORMS OPERATIONS GROUP BY -->


print("{:<15} {:<15}".format("EMP Count ","EMP Name"))
try:
    sql = "SELECT count(*), deptname from employee group by deptname"
    mycursor.execute(sql)
    sdata = mycursor.fetchall() 
    for s in sdata:
        print("{:<15} {:<15}".format(s[0], s[1]))
except:
    print("Error...")