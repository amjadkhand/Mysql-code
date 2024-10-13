import pymysql as mq

mysql = mq.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "school" 
)

mycursor = mysql.cursor()

print("{:<13} {:20}".format("State Id", "State Name"))

# try:
#     sql = "SELECT state_id, state_name from state"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()
#     for s in sdata:
#         print("{:<13} {:20}".format(s[0], s[1]))

# except:
#     print("Error....")


# <-- use between query -->


try:
    sql = "SELECT state_id, state_name from state where state_id between 2 and 5"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<13} {:20}".format(s[0], s[1]))

except:
    print("Error....")