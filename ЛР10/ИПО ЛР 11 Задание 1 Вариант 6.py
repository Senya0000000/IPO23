class Aviasales:
   '''Атрибуты:
   - proizvoditel: компания/производитель самолета
   - model: модель самолета
   - vmestimost: вместимость самолета
   - speed: скорость самолета
   - dalnost: дальность полета самолета
   - fuel: вместимость топливного бака
   Методы:
   - get_proizvoditel : Возвращает производителя самолета.
   - set_proizvoditel : Устанавливает производителя самолета.
   - get_model : Возвращает модель самолета.
   - set_model : Устанавливает производителя самолета.
   - get_vmestimost : Возвращает вместимость самолета.
   -set_vmestimost : Устанавливает вместимость самолета.
   -get_speed :  Возвращает скорость самолета
   -set_speed : Устанавливает скорость самолета.
   -get_dalnost : Возвращает дальность самолета
   -set_dalnost : Устанавливает дальноость самолета.
   -get_fuel : Возвращает вместимость топливного бака самолета самолета
   -set_fuel : Устанавливает вместимость топливного бака самолета.


   '''

   def __str__(self):
      """Возвращает строковое представление самолета."""
      return f"Самолет - Производитель: {self.proizvoditel},' \
              f'Модель: {self.model}, Вместимость: {self.vmestimost}, ' \
              f'Скорость: {self.speed}, Дальность полета: {self.dalnost}, ' \
              f'Вместимость топливного бака: {self.fuel}"
   def __init__(self, proizvoditel, model, vmestimost, speed, dalnost, fuel):
      self.proizvoditel = proizvoditel
      self.model = model
      self.vmestimost = vmestimost
      self.speed = speed
      self.dalnost = dalnost
      self.fuel = fuel
   def get_proizvoditel(self):
      """Возвращает производителя самолета."""
      return self.proizvoditel
   def set_proizvoditel(self, proizvoditel):
      '''Устанавливает производителя самолета.'''
      self.proizvoditel = proizvoditel
   def get_model(self):
      """Возвращает модель самолета."""
      return self.model
   def set_model(self, model):
      """Устанавливает производителя самолета."""
      self.model = model
   def get_vmestimost(self):
      """Возвращает вместимость самолета."""
      return self.vmestimost
   def set_vmestimost(self, vmestimost):
      """Устанавливает вместимость самолета."""
      self.vmestimost = vmestimost
   def get_speed (self):
      """Возвращает скорость самолета."""
      return self.speed
   def set_speed(self, speed):
      """Устанавливает скорость самолета."""
      self.speed = speed
   def get_dalnost(self):
      """Возвращает дальность полета  самолета."""
      return self.dalnoct
   def set_dalnost(self, dalnost):
      """Устанавливает дальность полета самолета."""
      self.dalnost = dalnost
   def get_fuel(self):
      """Возвращает топливо самолета."""
      return self.fuel
   def set_fuel(self, fuel):
      """Устанавливает топливо самолета."""
      self.fuel = fuel
   #вывод документации
print (Aviasales.__doc__)
#создаем экземпляр класса
plane1 = Aviasales("Boeing", "737", 180, 950, 3500, 20000)
plane2 = Aviasales("Airbus", "A320", 200, 920, 3000, 18000)
plane3 = Aviasales ("Embraer", "E190", 100, 850, 2500, 15000)
plane4 = Aviasales ("Bombardier", "CS300", 150, 880, 2800, 16000)
plane5 = Aviasales ("Sukhoi", "Superjet 100", 90, 870, 2700, 14000)
print(plane1)
print(plane2)
print(plane3)
print(plane4)
print(plane5)







