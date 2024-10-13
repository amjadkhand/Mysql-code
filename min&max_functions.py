import pymysql as mq


# <-- CREATE TABLE -->

mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ecomerce" 
)

mycursor = mysql.cursor() 

# tc = '''CREATE TABLE orders (
#     order_id INT PRIMARY KEY AUTO_INCREMENT,
#     order_date DATE,
#     user_id INTEGER,
#     order_amount INTEGER
   
# );'''

# mycursor.execute(tc)
# mysql.commit()



# <-- INSERT RECORD IN TABLE -->


# ins= "INSERT INTO orders (order_date,user_id, order_amount) values ('2024-10-13',3, 4000)"
# mycursor.execute(ins)
# mysql.commit()
# print("Insert Data ")
    


# <-- PERFORMS OPERATIONS -->

print("{:<15}".format("Order Total"))

try:
    sql = "SELECT order_amount from orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error...")


# <-- PERFORMS OPERATIONS MIN -->

# try:
#     sql = "SELECT min(order_amount) from orders"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
#     for s in sdata:
#         print("{:<15}".format(s[0]))
# except:
#     print("Error...")



# <-- PERFORMS OPERATIONS MAX -->

try:
    sql = "SELECT max(order_amount) from orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error...")