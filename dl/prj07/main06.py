#select

import oracledb


DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN  = "localhost:1521/xe"
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)

cursor = conn.cursor()
sql = "SELECT * FROM BOARD"
cursor.execute(sql)

result = cursor.fetchall()#cursor.fetchall()은 SELECT로 조회된 결과를 전부 가져오는 것
print(result)
cursor.close()
cursor = conn.cursor()

