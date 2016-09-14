import mysql.connector


config = {'user' : 'root', ' password': 'root','host' :'127.0.0.1', 'database':'PythonPractice', }

# cnx = mysql.connector.connect(*config)
cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='PythonPractice')

cursor = cnx.cursor()