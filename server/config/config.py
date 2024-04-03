from decouple import config

# conect database mariadb

USER_DB= config("USER_DB")
PASSWORD_DB= config("PASSWORD_DB")
HOST_DB= config("HOST_DB")
PORT_DB= int(config("PORT_DB"))
DATABASE= config("DATABASE")
