def Nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def Nok(a, b):
    return (a * b) // Nod(a, b)