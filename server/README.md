# Task server

tools

[![tools](https://skillicons.dev/icons?i=py,fastapi)]()


# installation
you have to python and pip with mariadb, and type this in your terminal
```bash
pip freeze -r requirements.txt
```

# run server
you have to create a .env file with password for your mariadb
```bash
USER_DB=root
PASSWORD_DB=your_password
HOST_DB=localhost
PORT_DB=3306
DATABASE=your_name_db
```

and now, you can try to the run server
```bash
uvicorn main:app --reload
```

you can visit the page http://localhost:8000/

# documentation
You only need to document three lines for each function.(optional)


# Thank you for reading
- for [@Corro-Kun](https://github.com/Corro-Kun)


