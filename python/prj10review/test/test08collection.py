# list , dictionary , set , tuple

def func01():
    a = [10,20,30,40,50]
    a.append(100)
    a.append(200)
    a.insert(2,777)
    # remove , pop , del , sort , sorted , reverse
    a[0] = 123
    print(a)
    # result = a.sort()
    print(a)
    # print(result)
    b = a

def func02():
    print("----- dict -----")
    person = {"name" : "hong" , "age" : 18 , "blood":"A"}
    person["age"] += 1
    print(person["name"])
    print(person["age"])
    print(person["blood"])
    # print(person["mbti"])
    print(person.get("mbti" , "음성"))
    print( "hong" in person )

def func02_1():
    x = {
        "board01" : {"title":"~~~" , "content":"~~~","writer":"zzz"} ,
        "p2" : {"name":"영희" , "age":21} ,
        "p3" : {"name":"미영" , "age":30} ,
    }
    print(x)

def func03():
    print("----- set -----")
    x = {10,20,30}
    y = {20,30,40}

    print(x - y)

def func04():
    x = 10,20,30
    x[0] = 123
    print(x[0])

func04()


