# match

month = 0
match month :
    case 1 | 3 | 5 | 7 | 8 | 10 | 12 : print(31)
    case 4 | 6 | 9 | 11: print(30)
    case 2 : print(28)
    case _ : print("그런 달은 없습니다. 1~12 중 입력하세요")
