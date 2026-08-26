# class , instance , attribute , method
# 상속

class Product:
    pass


class Snack(Product):
    def __init__(self):
        self.a = 3

    def hello(self):
        pass


obj = Snack()
print(obj.a)


