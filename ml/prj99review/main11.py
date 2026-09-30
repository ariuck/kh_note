#쓰레드
import threading

def hello(nickname:str = "guest"):
    print(f"hello {nickname}")
    pass

t1 = threading.Thread(target=hello, args=("hong",))
t1.start()