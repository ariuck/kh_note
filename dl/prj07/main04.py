#update

import oracledb

DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN  = "localhost:1521/xe"
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)

cursor = conn.cursor()

a = input("title : ")
b = input("id : ")

sql = "UPDATE BOARD SET TITLE = :t WHERE ID = :id"
sql_param = {
    "t" : a ,
    "id" : b ,
}
cursor.execute(sql, sql_param)

conn.commit()

cursor.close()
conn.close()