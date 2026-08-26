import random

from model.pokemon import Pikachu, Lizard, Turtle, Pokemon

user = None
com = None


def print_pokemon_list():
    print("----- POKEMON LIST -----")
    print("1.", Pikachu())
    print("2.", Lizard())
    print("3.", Turtle())
    print()


def select_user_pokemon():
    global user
    while True:
        num = int(input("원하는 포켓몬 번호 : "))
        match num:
            case 1:
                user = Pikachu()
            case 2:
                user = Lizard()
            case 3:
                user = Turtle()
            case _:
                print("잘못 입력하셨습니다.")
                continue
        break


def select_com_pokemon():
    global com
    num = random.randint(1,3)
    match num:
        case 1:
            com = Pikachu()
        case 2:
            com = Lizard()
        case 3:
            com = Turtle()

def attack(attacker , defender , num):
    # 동작 수행
    match num:
        case 1:
            attacker.tackle(defender)
        case 2:
            attacker.skill(defender)
    # 정보 출력
    print("attacker:",attacker)
    print("defender:",defender)
    # 결과 판단
    result = com.is_dead()
    if result:
        print(f"{user.name} 의 빅토리 !!!")
        return True

def battle_start():
    while True:
        # 사용자 차례
        print("----- 동작 선택 -----")
        print("1. 몸통박치기")
        print("2. 스킬")
        num = int(input("번호 : "))
        is_finish = attack(user, com, num)
        if is_finish: break
        # 컴퓨터 차례
        num = random.randint(1, 2)
        is_finish = attack(attacker=com, defender=user, num=num)
        if is_finish: break




def play_game():
    print("===== POKEMON =====")
    print_pokemon_list()
    select_user_pokemon()
    select_com_pokemon()
    battle_start()
