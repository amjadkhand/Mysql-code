import pymysql as mq

mysql = mq.connect(
      host="localhost",
    user="root",
    password="",
    database = "school"
)

# mycursor = mysql.cursor()

# tc = '''CREATE TABLE state (
#     state_id INT PRIMARY KEY AUTO_INCREMENT,
#     state_name VARCHAR(50),
#     country_id INTEGER,
     
#     FOREIGN KEY (country_id) REFERENCES country (country_id)) '''

# mycursor.execute(tc)
# mysql.commit()
# mysql.close()


# <-- INSERT RECORD INTO STATE TABLE -->


mycursor = mysql.cursor()

# try:
#     mycursor.execute('''
#     ins= "INSERT INTO state (state_id, state_name, country_id)  values ('Rajasthan', 3)"
    
# ''')
#     mysql.commit()
#     mysql.close()
#     print("Insert Data")
    
# except:
#     print('Error...')

mycursor.execute('''

INSERT INTO state (country_id, state_name) values (5, 'Shangai') 
''')
mysql.commit()
mysql.close()


