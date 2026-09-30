# conn 버전 확인

import oracledb

DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN  = "localhost:1521/xe"
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)


print(conn.version)

