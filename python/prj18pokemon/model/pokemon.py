from abc import abstractmethod, ABC


class Pokemon(ABC):
    def __init__(self, name, max_hp, atk, arm):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.atk = atk
        self.arm = arm

    def __str__(self):
        return f"{self.name} ({self.hp}/{self.max_hp})"

    def tackle(self, enemy):
        print("몸통 박치기 !!!")
        dmg = self.atk - enemy.arm
        if dmg < 1: dmg = 1
        enemy.hp -= dmg

    @abstractmethod
    def skill(self , enemy):
        pass

    def is_dead(self):
        return self.hp <= 0


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(max_hp=100, arm=3, atk=10, name="피카츄")

    def skill(self , enemy):
        print("백만볼트 !!!")
        dmg = self.atk * 2
        enemy.hp -= dmg


class Lizard(Pokemon):
    def __init__(self):
        super().__init__(max_hp=80, arm=2, atk=12, name="파이리")

    def skill(self , enemy):
        print("불꽃세례 !!!")
        dmg = self.atk * 3 - enemy.arm
        enemy.hp -= dmg


class Turtle(Pokemon):
    def __init__(self):
        super().__init__(max_hp=110, arm=4, atk=8, name="꼬부기")

    def skill(self, enemy):
        print("물대포 !!!")
        dmg = self.atk * 2 - enemy.arm
        enemy.hp -= dmg
        self.hp += int(round(dmg * 0.3 , 0))
