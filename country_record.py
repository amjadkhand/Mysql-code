import pymysql as mq

# conn = mq.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "",
#     database = "school" 
# )

# mysqlc = conn.cursor()

# tc = '''CREATE TABLE country (
#     country_id INT PRIMARY KEY AUTO_INCREMENT,
#     country_name VARCHAR(50) 
#       ) '''

# mysqlc.execute(tc)
# conn.commit()



# <-- INSERT RECORD INTO COUNITRY TABLE -->


mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school" 
)

mysqlc = mysql.cursor()

try:
    ins= "INSERT INTO country (country_name)  values (%s)"

    tup = ("Afghanistan"),("China")
    mysqlc.executemany(ins,tup)
    mysql.commit()
    print("Insert Data")
    
except:
    print('Error...')