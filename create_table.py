import pymysql as mq

conn = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school" 
)

mysqlc = conn.cursor()

tc = '''CREATE TABLE student (
    st_id INT PRIMARY KEY AUTO_INCREMENT,
    st_name VARCHAR(50),
    st_class VARCHAR(10),
    st_email VARCHAR(50)
);'''

mysqlc.execute(tc)
conn.commit()  # Don't forget to commit the transaction