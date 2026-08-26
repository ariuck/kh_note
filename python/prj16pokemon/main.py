import random

from model.lizard import Lizard
from model.pikachu import Pikachu
from model.pokemon import Pokemon
from model.turtle import Turtle


def battle(attacker, defender):
    print(f"\"{attacker.name}\" 가 \"{defender.name}\" 를 공격 !")
    defender.hp -= attacker.atk
    print("attacker : ", attacker)
    print("defender : ", defender)


# 포켓몬 객체들 생성
p1 = Pikachu()
p2 = Lizard()
p3 = Turtle()

# 포켓몬 목록 출력
print("----- pokemon list -----")
print(1, p1)
print(2, p2)
print(3, p3)
print()

# 유저 포켓몬 선택
user = None
num = int(input("원하는 포켓몬 번호 : "))
match num:
    case 1:
        user = Pikachu()
    case 2:
        user = Lizard()
    case 3:
        user = Turtle()

com = None
num = random.randint(1, 3)
match num:
    case 1:
        com = Pikachu()
    case 2:
        com = Lizard()
    case 3:
        com = Turtle()

while True:
    # 유저가 컴퓨터공격
    battle(user, com)
    if com.hp <= 0: break

    # 컴퓨터가 공격
    battle(com, user)
    if user.hp <= 0: break
