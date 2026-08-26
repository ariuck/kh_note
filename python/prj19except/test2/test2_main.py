def f01():
    print("f01 called ~~~")
    try:
        f02()
    except Exception as e:
        print("f02 너 그럴줄 알았다 ,,,에러났네 ,,,", e)
    print("f01 finish !!!")


def f02():
    print("f02 called ~~~")
    raise Exception("errrrrr~@@!!@!@!!@!@!@!@")
    f03()
    print("f02 finish !!!")


def f03():
    print("f03 called ~~~")
    print("f03 finish !!!")


f01()
