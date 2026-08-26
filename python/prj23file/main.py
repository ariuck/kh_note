from book import Book
import json


def write_to_file():
    with open("data.txt", "w", encoding="utf-8") as f:
        title = input("title :  ")
        price = int(input("price :  "))
        book = Book(title, price)
        json.dump(book.to_dict(), f, ensure_ascii=False, indent=2)


def read_from_file():
    with open("data.txt", "r", encoding="utf-8") as f:
        d = json.load(f)
        print(d)
        book = Book.from_dict(d)
        print(book.title)
        print(book.price)


while True:
    print("0. exit")
    print("1. write")
    print("2. read")
    num = int(input("메뉴 번호 : "))
    match num:
        case 0:
            break
        case 1:
            write_to_file()
        case 2:
            read_from_file()

# try:
#     f = open("data.txt" , "a" , encoding="utf-8")
#     f.write("\nasdfjhkkasdjlfasdhkjlgfasdhjkgf\n")
# finally:
#     f.close()
