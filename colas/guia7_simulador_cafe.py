import random
from collections import deque

random.seed(42)                     # para reproducibilidad
cola = deque([f"Cliente-{i+1}" for i in range(10)])

# Dos cajas: cada una guarda (cliente, tiempo_restante) o None si libre
cajas = [None, None]

segundo = 0

while cola or any(cajas):
    # Cada caja libre agarra al primero
    for i in range(2):
        if cajas[i] is None and cola:
            cliente = cola.popleft()
            tiempo = random.randint(30, 90)
            cajas[i] = [cliente, tiempo]
            print(f"[{segundo}s] Caja {i+1}: atendiendo a {cliente} ({tiempo}s)")

    # Cada caja ocupada trabaja 1 segundo
    for i in range(2):
        if cajas[i]:
            cajas[i][1] -= 1
            if cajas[i][1] == 0:
                print(f"[{segundo+1}s] Caja {i+1}: terminó con {cajas[i][0]}")
                cajas[i] = None

    segundo += 1

print(f"\nTiempo total: {segundo}s")