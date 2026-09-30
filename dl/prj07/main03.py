# insert

import oracledb

DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN  = "localhost:1521/xe"
conn = oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)

cursor = conn.cursor()#커서를 사용(설명 안해주심)

a = input("title : ")
b = input("content : ")
#sql = "게시글 작성하는 줄 복붙"
#********* 복붙할때 세미콜론 꼭!!! 빼야함 ************
sql = "INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(1, :t, :c)"
#원래는 sql문은 줄빠꿈해서 작성해서 ''' ''' 이걸 사용해서 함, 근데 원래원래 최근에는 딴거 쓴다함

#바인드 변수 :SQL문 안에 값을 직접 쓰지 않고, 나중에 넣을 자리만 표시해두는 변수
sql_param = {
    "t" : a ,
    "c" : b ,
}
cursor.execute(sql, sql_param)
result = cursor.rowcount#몇개의 행을 건드는지 확인
print(result)#이걸 확인해서 정상작동했는지 확인

#여기 단계에서는 실행되지 않음 insert 적용x 트랜잭션(Transaction) 작업필요
# 트랜잭션을 해야함 트랜잭션은 DB에서 여러 작업을 하나의 묶음으로 처리하는 것
# 코드상의 작업레벨 단위라 트랜잭션 해줘야함 논리상적인 작업
# ex) 주문 작업(논리 작업)
# 을 하려면 코드상으로 코드 레벨의 작업(재고확인, 셀렉트, 재고 없으면 충전, 쿠폰 조회, 쿠폰 사용처리, 결제 업데이트,업데이트 된 주문내역서 머니차감 배송)
# 을 함 그래서 한 코드 레벨의 작업을 한다고 적용x
# 쿼리문 하나 실행해서 실행되는게 아님
# 그렇기 때문에 트랜잭션인 컷밋까지 하여 디비에 반영

conn.commit()# 커밋 디비에 반영
# 커넥션.롤백하면 마지막 커밋지점으로 돌아감

#현재 실행에서는 문제 없지면 실제 서비스에서 반드시 해야함
cursor.close()
conn.close()