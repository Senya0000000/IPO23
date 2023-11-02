N = int(input("Введите количество чисел: "))  # Вводим N с клавиатуры
numbers = []  # Создаем пустой список для хранения чисел
# Вводим числа и добавляем их в список
for _ in range(N):
    num = int(input("Введите число: "))
    numbers.append(num)
# Записываем числа в файл file1_NN.txt
file_txt = f"file1_{N}.txt"
with open(file_txt, "w") as file1:
    for num in numbers:
        file1.write(str(num) + "\n")
# Вычисляем сумму и произведение чисел
summation = sum(numbers)
product = 1
for num in numbers:
    product *= num
# Записываем сумму и произведение в файл file2_NN.txt
file2_txt = f"file2_{N}.txt"
with open(file2_txt, "w") as file2:
    file2.write(f"Сумма: {summation}\n")
    file2.write(f"Произведение: {product}\n")
print(f"Сумма чисел: {summation}")