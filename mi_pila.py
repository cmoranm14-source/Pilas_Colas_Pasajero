from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1] = None
        self.cantidad -= 1 
        return pasajero 
    
    def ver_tope(self):
        if self.cantidad == None:
            return None
        return self.datos[self.cantidad-1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return self.datos[i]
        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False
        pasajero.destino = nuevo_destino
        pasajero.asiento = nuevo_asiento

    def eliminar_por_numero(self, numero):
        auxiliar = [None] * self.capacidad
        tope_auxiliar = 0
        encontrado = False
        while self.cantidad > 0:
            elemento_actual = self.datos[self.cantidad - 1]
            self.datos[self.cantidad - 1] = None 
            self.cantidad -= 1 
            if elemento_actual.numero == numero and not encontrado:
                encontrado = True 
            else:
                auxiliar[tope_auxiliar] = elemento_actual
                tope_auxiliar += 1
        for i in range(0, tope_auxiliar):
            self.datos[self.cantidad] = auxiliar[i]
            self.cantidad += 1
        return encontrado


    def copiar(self):
        nueva = MiPila(self.cantidad)
        for pasajero in range(self.cantidad):
            nueva.apilar(self.datos[pasajero])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.datos == 0