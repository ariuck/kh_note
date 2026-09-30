from swy.memberVo import MemberVo
import oracledb


def join_r(vo:MemberVo) -> int:

    conn = oracledb.connect(
        user="C##KH",
        password="1234",
        dsn="localhost:1521/xe",
    )
    cursor = conn.cursor()

    sql = "INSERT INTO MEMBER(ID,PW,NICK) VALUES (:1,:2,:3)"
    cursor.execute(sql , [vo.id, vo.pw, vo.nick])
    result = cursor.rowcount

    conn.commit()
    cursor.close()
    conn.close()
    return result

