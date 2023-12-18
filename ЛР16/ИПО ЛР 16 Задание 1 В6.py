class Product:
    def __init__(self, name, price, quantity, category):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
        else:
            raise ValueError("Quantity cannot be negative")
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        self._category = value
# Создание объекта с использованием конструктора
product1 = Product("Phone", 500, 10, "Electronics")
print(product1.name, product1.price, product1.quantity, product1.category)

# Изменение значений свойств с использованием сеттеров
product1.price = 600
product1.quantity = 5
print(product1.name, product1.price, product1.quantity, product1.category)

# Попытка изменения значения свойства напрямую (вызовет ошибку)
product1.quantity = -5