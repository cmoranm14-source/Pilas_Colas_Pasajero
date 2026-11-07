from collections import deque

def binario_a_decimal(s):
    if s == "0":
        return 0

    pila = deque()

    for digito in s:
        pila.append(int(digito))

    decimal = 0
    potencia = 1

    while pila:
        residuo = pila.pop()
        decimal += residuo * potencia
        potencia = potencia * 2  

    return decimal

print(binario_a_decimal('1101'))
