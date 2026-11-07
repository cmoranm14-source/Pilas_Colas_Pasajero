from collections import deque

class ColaPrioridad:
    def __init__(self, niveles=3):
        # Un deque por cada nivel (índice = prioridad, más alto = más urgente)
        self.niveles = niveles
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, valor, prioridad):
        if not 0 < prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")
        self.colas[prioridad].append(valor)

    def desencolar(self):
        """Saca el de mayor prioridad; entre iguales, el más antiguo."""
        # Recorremos de la prioridad más alta a la más baja
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                return self.colas[i].popleft()
        raise IndexError("Cola vacía")
    def cambiar_prioridad(self, valor, nueva_prioridad):
        # 1. Busca en todas las colas y borra al elemento si lo encuentra
        for i in range(1, self.niveles + 1):
            if valor in self.colas[i]:
                self.colas[i].remove(valor)
                break  # Ya lo borró, sale del bucle

        # 2. Lo mete en su nueva cola usando tu misma función 'encolar'
        self.encolar(valor, nueva_prioridad)


    def __str__(self):
        s = []
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                s.append(f"  P{i}: {list(self.colas[i])}")
        return "\n".join(s) if s else "(vacía)"


# --- Uso ---
cp = ColaPrioridad(3)
cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

print(cp)
# P3: ['Luis']
# P2: ['Beto']
# P1: ['Ana', 'Diana']

# Atender en orden
while True:
    try:
        print("Atendiendo:", cp.desencolar())
    except IndexError:
        break
# Luis / Beto / Ana / Diana