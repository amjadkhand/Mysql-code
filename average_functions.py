import pymysql as mq

mysql = mq.connect(
      host="localhost",
    user="root",
    password="",
    database = "ecomerce"
)

mycursor = mysql.cursor()


# print("{:<15}".format("Order Avg"))
# try:
#     sql = "SELECT order_amount from orders"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall() 
#     for s in sdata:
#         print("{:<15}".format(s[0]))
# except:
#     print("Error...")



 # <-- PERFORMS OPERATIONS Average -->      


try:
    sql = "SELECT avg(order_amount) from orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall() 
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error...")