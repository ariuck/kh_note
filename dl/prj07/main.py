#prj06에서는 gpu연산을 사용하기 위해 3.12버전을 사용 여기는 아무 버전이나 사용 가능

#=========py - DB 연결==========

#Oracle SQL Developer 사용
#table 조회,계시, 작성

#SQL DB작성 후 돌아와서 PY - DB연결 작업

# 터미널 pip install oracledb

import oracledb

#변수를 대문자로 바꿔서 상수 취급 하자 : ctrl + shift + u (재할당이 안 되는 건 아님)
DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN = "localhost:1521/xe" #ip:port/sid(버전인듯)", 포트는 그냥 강사님이 이걸로 되있을 거라고 알려주심

#DB랑 연동하면 conn커넥션 객체 하나 생성
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)#연결 완료 ,()는 어떤 컴퓨터에 연결할지 내용

print(conn.version)#연결 확인