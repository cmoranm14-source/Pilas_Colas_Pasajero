from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[0]
        for i in range(1, self.cantidad):
            self.datos[i - 1] = self.datos[i]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero  

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for posicion in range(self.cantidad):
            if self.datos[posicion].numero == numero:
                return posicion
        return None 
    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio    
            elif self.datos[medio].numero < numero:
                izq = medio + 1 
            else:
                der = medio - 1
        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)
        if pasajero is None:
            return None
        pasajero.destino = nuevo_destino
        pasajero.asiento = nuevo_asiento

    def eliminar_por_numero(self, numero):
        encontrado = False
        for i in range(self.cantidad):
            pasajero_actual = self.desencolar()
            if pasajero_actual.numero == numero and not encontrado:
                encontrado = True
            else:
                self.encolar(pasajero_actual)
        return encontrado
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero > self.datos[i + 1].numero:
                    aux = self.datos[i]       
                    self.datos[i] = self.datos[i + 1] 
                    self.datos[i + 1] = aux
        pass

    def ordenar_desc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero < self.datos[i + 1].numero:
                    aux = self.datos[i]                
                    self.datos[i] = self.datos[i + 1]  
                    self.datos[i + 1] = aux

    def copiar(self):
        nueva = MiCola()
        for pasajero in range(self.cantidad):
            nueva.encolar(self.datos[pasajero])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
