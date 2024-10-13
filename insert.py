import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school"
    )

mycursor = mysql.cursor()

try:
    ins= "INSERT INTO student (st_name,st_class, st_email) values (%s, %s, %s) "

    tup = ('Waqar', '12th', 'waqar@gmail.com')
    mycursor.execute(ins,tup)
    mysql.commit()
    print("Insert Data ")
    
except:
    print('Error...')


# <-- MANY ENTRIES INSERT DATA INTO student TABLE -->

# try:
#     ins= "INSERT INTO student (st_name,st_class, st_email) values (%s, %s, %s) "

#     tup = ('noman', '12th', 'noman@gmail.com'),('zahid', '12th', 'zahid@gmail.com')
#     mycursor.executemany(ins,tup)
#     mysql.commit()
#     print("Insert Data ")
    
# except:
#     print('Error...')