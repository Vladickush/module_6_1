# Задача "Мифическое наследование":
class Horse:
    x_distance = 0  # пройденный путь.
    sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0  # высота полёта
    sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
