import os
import datetime
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
        row = ("Bob", 21, "1990-02-06 23:04:56")    
        cursor.execute(" INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()

finally:
    # close the connection regardless of whether the above
    # was successful or not
    connection.close()
