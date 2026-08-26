# 자판기

menu = '''
======= 자판기 =======
1. 콜라     1500원
2. 사이다   1300원
3. 커피     2000원
4. 잔액조회
0. 종료
======================
'''

money = 10000

while True:
    # 메뉴판 출력
    print(menu)

    # 유저 메뉴 입력받기
    num = int(input("메뉴번호 : "))

    # 메뉴번호에 따라서 동작
    if num == 1 :
        if money < 1500 :
            print("돈 없음")
        else :
            money -= 1500
        print("1500 원 차감")
    elif num == 2 :
        money -= 1300
        print("1300 원 차감")
    elif num == 3:
        money -= 2000
        print("2000 원 차감")
    elif num == 4:
        print(money)
    elif num == 0:
        print("프로그램 종료")
        break


