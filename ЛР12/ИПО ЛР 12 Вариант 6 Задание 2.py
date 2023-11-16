class Aviasales:
    def __init__(self, proizvoditel=None, model=None, vmestimost=None, speed=None, dalnost=None, fuel=None):
        self.proizvoditel = proizvoditel
        self.model = model
        self.vmestimost = vmestimost
        self.speed = speed
        self.dalnost = dalnost
        self.fuel = fuel
    def __str__(self):
        """Возвращает строковое представление самолета."""
        return f"Самолет - Производитель: {self.proizvoditel}, Модель: {self.model}, Вместимость: {self.vmestimost}, " \
               f"Скорость: {self.speed}, Дальность полета: {self.dalnost}, " \
               f"Вместимость топливного бака: {self.fuel}"
    def __del__(self):
        print(f"Деструктор класса выполнен для {self.proizvoditel},{self.model}")
    @property
    def proizvoditel(self):
        return self._proizvoditel
    @proizvoditel.setter
    def proizvoditel(self, proizvoditel):
        self._proizvoditel = proizvoditel
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        self._model = model
    @property
    def vmestimost(self):
        return self._vmestimost
    @vmestimost.setter
    def vmestimost(self, vmestimost):
        self._vmestimost = vmestimost
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        self._speed = speed
    @property
    def dalnost(self):
        return self._dalnost
    @dalnost.setter
    def dalnost(self, dalnost):
        self._dalnost = dalnost
    @property
    def fuel(self):
        return self._fuel
    @fuel.setter
    def fuel(self, fuel):
        self._fuel = fuel
# Создание списка объектов
planes = [Aviasales("Boeing", "747", 416, 917, 14815, 183380),
          Aviasales("Airbus", "A380", 853, 1,111, 15700),
          Aviasales("Boeing", "777", 396, 905, 15500, 181280),
          Aviasales("Airbus", "A350", 440, 945, 15000, 158800),
          Aviasales("Boeing", "787", 242, 913, 15700, 126372),
          Aviasales("Airbus", "A320", 180, 828, 6100, 23800),
          Aviasales("Boeing", "737", 200, 871, 5600, 20810),
          Aviasales("Airbus", "A220", 160, 829, 6045, 21500),
          Aviasales("Boeing", "727", 189, 965, 4278, 16600),
          Aviasales("Airbus", "A300", 266, 851, 7500, 47000)]
# Вывод списка объектов
for plane in planes:
    print(plane)