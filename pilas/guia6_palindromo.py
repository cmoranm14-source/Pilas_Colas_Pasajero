from collections import deque

def es_palindromo(s):
    s = s.lower().replace(" ", "")     # normaliza
    pila = deque()

    # Apila la mitad izquierda
    mitad = len(s) // 2
    for i in range(mitad):
        pila.append(s[i])

    # Compara con la mitad derecha (saltando el central si len es impar)
    inicio_der = mitad + (1 if len(s) % 2 == 1 else 0)
    for i in range(inicio_der, len(s)):
        if pila.pop() != s[i]:
            return False
    return True


for p in ["ana", "reconocer", "python", "anita lava la tina"]:
    print(f"{p!r}: {es_palindromo(p)}")