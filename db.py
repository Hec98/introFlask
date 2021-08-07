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

def insertData(user, email, age):
    sql = 'INSERT INTO Usuario (username, email, age) VALUES (%s, %s, %s)'
    values = (user, email, age)
    cursor.execute(sql, values)
    myDB.commit()
    return cursor.rowcount
