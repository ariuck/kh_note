from view.book_view import print_menu, scan_menu_num, process

# 도서 관리 프로그램
print("===== 도서 관리 프로그램 =====")
while True:
    print_menu()
    x = scan_menu_num()
    is_exit = process(x)
    if is_exit: break
