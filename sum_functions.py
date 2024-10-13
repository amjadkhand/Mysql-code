import pymysql as mq

mysql = mq.connect(
      host="localhost",
    user="root",
    password="",
    database = "ecomerce"
)

mycursor = mysql.cursor()


print("{:<15}".format("Order Amount"))
# try:
#     sql = "SELECT order_amount from orders"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall() 
#     for s in sdata:
#         print("{:<15}".format(s[0]))
# except:
#     print("Error...")



 # <-- PERFORMS OPERATIONS SUM -->      


try:
    sql = "SELECT sum(order_amount) from orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall() 
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error...")