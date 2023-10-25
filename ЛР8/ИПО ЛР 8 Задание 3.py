sequence = input('введтте последовательность символов ')
result_set=set()
for char in sequence:
    if char.isdigit() and int(char) % 2 == 0: #проверяем является ли цифра четной
        result_set.add(char)
    elif char == 'A':
        result_set.add(char)
        print ('множество элементов', char)