import pymysql as mq

mysql = mq.connect(
      host="localhost",
    user="root",
    password="",
    database = "ecomerce"
)

mycursor = mysql.cursor()


# print("{:<15} {:<15} {:<15}".format("Order Id", "Order Date", "Order Amount"))

# try:
#     sql = "SELECT order_id, order_date, order_amount from orders"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall() 
#     for s in sdata:
#         print("{:<15} {:<15} {:<15} ".format(s[0],s[1],s[2]))
# except:
#     print("Error...")



 # <-- PERFORMS OPERATIONS in -->      


# print("{:<15} {:<15} {:<15}".format("Order Id", "Order Date", "Order Amount"))

# try:
#     sql = "SELECT order_id, order_date, order_amount from orders where order_id in(1,6)"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall() 
#     for s in sdata:
#         print("{:<15} {:<15} {:<15} ".format(s[0],s[1],s[2]))
# except:
#     print("Error...")




 # <-- PERFORMS OPERATIONS Not in -->      


print("{:<15} {:<15} {:<15}".format("Order Id", "Order Date", "Order Amount"))

try:
    sql = "SELECT order_id, order_date, order_amount from orders where order_id not in(1,6)"
    mycursor.execute(sql)
    sdata = mycursor.fetchall() 
    for s in sdata:
        print("{:<15} {:<15} {:<15} ".format(s[0],s[1],s[2]))
except:
    print("Error...")