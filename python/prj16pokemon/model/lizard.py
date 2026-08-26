class Lizard:
    def __init__(self):
        self.name = "Lizard"
        self.hp = 90
        self.atk = 11

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"