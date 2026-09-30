from dataclasses import dataclass
from traceback import print_tb
from unittest import case
import oracledb

@dataclass
class BoardVO:
    id: int
    title: str
    content: str


def get_conn():
    DB_USER = "C##KH"
    DB_PASSWORD = "1234"
    DB_DSN  = "localhost:1521/xe"
    return oracledb.connect(user=DB_USER,password=DB_PASSWORD, dsn=DB_DSN)

def print_menu():
    print()
    print("========== M E N U ==========")
    print("0. exit")
    print("1. insert_board")
    print("2. update_board_title")
    print("3. delete_board_by_id")
    print("4. select_board_one")
    print("5. select_board_list")

def choose_menu():
    print_menu()
    num = int(input("menu num : "))

    match num:
        case 0:
            return True
        case 1:
            insert_board()
            return  False
        case 2:
            update_board_title()
            return False
        case 3:
            delete_board_by_id()
            return False
        case 4:
            select_board_one()
            return False
        case 5:
            select_board_list()
            return False
        case _:
            print("wrong number")
            return False

def insert_board():
    print("----- 게시글 작성 -----")
    conn = get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO BOARD ( ID , TITLE , CONTENT ) VALUES ( SEQ_BOARD.NEXTVAL , :title , :content )"
    sql_param = {
        "title" : "파이썬~~~",
        "content" : "ㅋㅋㅋ",
    }
    cursor.execute(sql, sql_param)
    conn.commit()
    print("게시글 작성 성공~~!")
    cursor.close()
    conn.close()


    #이게 정석
    # conn = get_conn()
    # cursor = conn.cursor()0

    #
    # try:
    #     sql = ""
    #     sql_param = {}
    #     cursor.execute(sql, sql_param)
    #     result = cursor.rowcount
    #
    #     if result > 0:
    #         conn.commit()
    #     else:
    #         conn.rollback()
    #
    # except Exception as e:
    #     conn.rollback()
    #
    # finally:
    #     cursor.close()
    #     conn.close()


def update_board_title():
    print("update board title ~~~")


def delete_board_by_id():
    print("delete board ~~~")


def select_board_one():
    print("----- 게시글 상세조회 -----")
    id = int(input("조회할 게시글 번호 : "))
    conn = get_conn()
    cursor = conn.cursor()
    sql = "SELECT * FROM BOARD WHERE ID = :id"
    sql_param = {"id" : id}
    cursor.execute(sql, sql_param)
    row = cursor.fetchone()
    print(row)
    cursor.close()
    conn.close()




def select_board_list():
    print("----- 게시글 목록조회 -----")
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOARD ORDER BY ID DESC")

    col_name_list = []
    for x in cursor.description:
        col_name = x[0].lower()
        col_name_list.append(col_name)

    row_list = cursor.fetchall()

    vo_list = []
    for row in row_list:
        d = dict(zip(col_name_list, row))
        vo = BoardVO(**d)
        vo_list.append(vo)

    print(vo_list)


    col_name_list = []
    for x in cursor.description:
        col_name = x[0]
        col_name_list.append(col_name)
    print(col_name_list)


    cursor.close()
    conn.close()


while True:
    is_break = choose_menu()

    if is_break == True:
        break

