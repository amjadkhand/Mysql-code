import pymysql as mq

mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ecomerce" 
)

mycursor = mysql.cursor()

try:
    sql= "SELECT * from categories as c1, categories as c2 where c1.cat_id = c2.prent_id"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for a in sdata:
        print(a)
    
except:
    print('Error...')