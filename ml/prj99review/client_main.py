import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.40.3" , 9876))

nickname = input("nickname : ")
client_socket.send(nickname.encode())
def receive():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("not data : ", data)
                print("상대방 나감")
                break
            print(data.decode())
        except Exception as e:
            print("예외발생 !!!", e)
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    # 발신
    msg = input("보낼 메세지 : ")
    msg = f"\n[{nickname}] :{msg}"
    client_socket.send(msg.encode())