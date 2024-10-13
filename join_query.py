import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database = "school"
    )

mycursor = mysql.cursor()

print("{:<13} {:20} {:20}".format("State Id", "State Name", "Country Id"))

# try:
#     sql = "Select * from state"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()

#     for s in sdata:
#          print("{:<13} {:20} {:20}".format(s[0], s[1], s[2]))
# except:
#     print("Error....")


# <-- Inner Join --> 


# try:
#     sql = "Select * from state inner join country on state.country_id = country.country_id"
#     mycursor.execute(sql)
#     sdata = mycursor.fetchall()

#     for s in sdata:
#          print(s)
#          print("{:<13} {:20} {:20}".format(s[0], s[1], s[2]))
# except:
#     print("Error....")



# <-- To get specifif data using Inner Join --> 


try:
    sql = "Select state.state_id, state.state_name, country.country_name from state inner join country on state.country_id = country.country_id"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
         print(s)
         print("{:<13} {:20} {:20}".format(s[0], s[1], s[2]))
except:
    print("Error....")