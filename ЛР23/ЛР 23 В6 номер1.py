import numpy as np

# Генерация случайного количества строк и столбцов
rows = np.random.randint(15, 101)
cols = np.random.randint(15, 101)

# Создание прямоугольного массива
arr = np.random.randint(1, 1001, size=(rows, cols))

# Вывод массива на экран
print(arr)

# Поиск минимального элемента в строке 6
min_element = np.min(arr[5, :])

# Вывод минимального элемента
print("Минимальный элемент в строке 6:", min_element)

# Умножение матрицы на минимальный элемент
result = arr * min_element

# Вывод результата на экран
print("Результат умножения на минимальный элемент:")
print(result)
