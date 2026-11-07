from collections import deque

def evaluar_postfija(expr):
    pila = deque()
    for token in expr.split():
        if token in "+-*/":
            b = pila.pop()      # OJO al orden: b sale primero
            a = pila.pop()
            if token == "+": pila.append(a + b)
            elif token == "-": pila.append(a - b)
            elif token == "*": pila.append(a * b)
            elif token == "/": pila.append(a / b)
        else:
            pila.append(int(token))
    return pila.pop()


print(evaluar_postfija("3 4 +"))         # 7
print(evaluar_postfija("3 4 + 5 *"))     # 35
print(evaluar_postfija("5 1 2 + 4 * + 3 -"))  # 14