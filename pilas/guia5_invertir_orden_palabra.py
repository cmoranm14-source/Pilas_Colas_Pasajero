from collections import deque

def invertir_palabras(frase):
    pila = deque()
    for palabra in frase.split():
        pila.append(palabra)

    resultado = []
    while pila:
        resultado.append(pila.pop())
    return " ".join(resultado)


print(invertir_palabras("Hola Mundo desde Python"))
