import os
import pymysql

# get username from could9 workspace
#(modify variable if running on another environment)

username = os.getenv('c9_user')

#connect to the database

connection = pymysql.connect(host='localhost',
                            user = username,
                            password = "",
                            db = "Chinook")

try:
    # Run a Query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection regardless of whether the above
    #was successful or not
    connection.close()
