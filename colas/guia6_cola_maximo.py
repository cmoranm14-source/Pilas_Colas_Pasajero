from collections import deque

class ColaConMax:
    def __init__(self):
        self._datos = deque()
        self._max_visto = float("-inf")

    def encolar(self, v):
        self._datos.append(v)
        if v > self._max_visto:
            self._max_visto = v

    def desencolar(self):
        if not self._datos:
            raise IndexError("vacía")
        return self._datos.popleft()

    def maximo_visto(self):
        return self._max_visto


c = ColaConMax()
for x in [5, 3, 8, 2]:
    c.encolar(x)
while c._datos:
    print(c.desencolar())
print("Máximo visto:", c.maximo_visto())