from collections import deque

jugadores = deque(["Ana", "Beto", "Carlos"])

for turno in range(10):
    actual = jugadores.popleft()      # sale del frente
    print(f"Turno {turno+1}: {actual}")
    jugadores.append(actual)          # vuelve al final