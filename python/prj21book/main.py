# 도서 관리
from book_manager import print_menu, scan_user_input, process

print("===== 도서 관리 프로그램 =====")

while True:
    try:
        print_menu()
        num = scan_user_input()
        process(num)
    except Exception as e :
        print(e)