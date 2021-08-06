import mysql.connector as mysqlDB

myDB = mysqlDB.connect(
    host = 'localhost',
    user = 'root',
    password = 'toor',
    database = 'prueba'
)
cursor = myDB.cursor(dictionary = True)

def selectDataBase():
    cursor.execute('SELECT * FROM Usuario')
    result = cursor.fetchall()
    return result
