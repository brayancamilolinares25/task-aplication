from mariadb import connect, Error
from config.config import DATABASE, HOST_DB, PASSWORD_DB, PORT_DB, USER_DB 

 try:
    conn = connect(
        user= USER_DB,
        password= PASSWORD_DB,
        host= HOST_DB,
        port= PORT_DB,
        database= DATABASE,
    )
except Error as e:
    print(e)

cur = conn.cursor(dictionary=True)
