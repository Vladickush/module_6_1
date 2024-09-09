# Задача "Съедобное, несъедобное":
class Animal:       # животное
    alive = True    # живое
    fed = False     # накормленное
    def __init__(self, name):
        self.name = name    # название животного


class Mammal(Animal):               # млекопитающее
    def eat(self, food):            # ест фрукт
        if Fruit.edible == True:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False


class Predator(Animal):             # хищник
    def eat(self, food):            # ест цветок
        if Flower.edible == True:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False


class Plant:                # растение
    def __init__(self, name):
        self.name = name    # название растения


class Flower(Plant):        # цветок
    edible = False          # несъедобный


class Fruit(Plant):         # фрукт
    edible = True           # съедобный


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
