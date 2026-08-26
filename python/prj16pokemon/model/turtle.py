class Turtle:
    def __init__(self):
        self.name = "Turtle"
        self.hp = 110
        self.atk = 9

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"