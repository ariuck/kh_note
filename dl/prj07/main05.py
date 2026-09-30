#delete

import oracledb

DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN  = "localhost:1521/xe"
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)

cursor = conn.cursor()

a = input("id : ")

sql = "DELETE BOARD WHERE ID = :id"
sql_param = {
    "id" : a ,
}
cursor.execute(sql, sql_param)

conn.commit()

cursor.close()
conn.close()

#dml 한거임 지금까지