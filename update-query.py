import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school")

mycursor = mysql.cursor()

name = input("Enter the Student Name:- ")
class_name = input("Enter the Class Name:- ")
st_email = input("Enter the Student Email:- ")
st_id = input("Enter the Student Id:- ")


sql = "UPDATE student set st_name=%s, st_class=%s,st_email=%s where st_id=%s"
data = (name, class_name, st_id, st_email)

try:
    mycursor.execute(sql, data)
    mysql.commit()

    print("Record Updated")
except:
    print("Error....")