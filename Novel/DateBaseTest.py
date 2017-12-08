import pymysql

db=pymysql.connect("localhost","root","334455","reptile")
db.encoding='utf-8'
cursor=db.cursor()
cursor.execute('SET NAMES utf8')
sql="select book_name from test"
cursor.execute(sql)
result=cursor.fetchall()
print(result)