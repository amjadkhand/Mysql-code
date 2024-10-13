import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school")

mycursoer = mysql.cursor()
st_id = input("Enter the Student Id ")
sql = "DELETE FROM student where st_id=%s"

try:
    mycursoer.execute(sql, st_id)
    mysql.commit()
    print("Record Deleted")

except:
    print("Error...")
