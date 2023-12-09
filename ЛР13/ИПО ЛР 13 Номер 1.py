class Drob(object):
    """ Дробь вида a/b"""
    def __init__(self, a=0, b=1):
        if b == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен 0")
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        gcd = self.gcd(abs(self.a), abs(self.b))
        self.a //= gcd
        self.b //= gcd
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def gcd(self, a, b):
        """Находит наибольший общий делитель для a и b"""
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __add__(self, other):
        n = self.a * other.b + other.a * self.b
        d = self.b * other.b
        return Drob(n, d)

    def __sub__(self, other):
        n = self.a * other.b - other.a * self.b
        d = self.b * other.b
        return Drob(n, d)

    def __mul__(self, other):
        n = self.a * other.a
        d = self.b * other.b
        return Drob(n, d)

    def __truediv__(self, other):
        n = self.a * other.b
        d = self.b * other.a
        return Drob(n, d)
a = Drob(2, 3)
b = Drob(3, 4)

print(a == Drob(2, 3))  # True
print(a == b)  # False
print(a < b)  # True
print(a + b)  # 17/12
print(a - b)  # -1/12
print(a * b)  # 1/2
print(a / b)  # 8/9