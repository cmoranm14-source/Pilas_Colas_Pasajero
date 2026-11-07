from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from utils import confirmar, imprimir_error, imprimir_exito, imprimir_info, imprimir_titulo, limpiar_pantalla

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def pausa():
    input("\nPresione Enter para continuar...")
    
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver, extras = False):
    imprimir_titulo(f" {titulo} ")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    if extras:
        print("10. Buscar binaria               11. Ordenar asc")
        print("12. Ordenar desc ")
    print(" C. Cargar datos de prueba                0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                imprimir_exito("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            if pila.desapilar():
                imprimir_exito(" Desapilado: se quito el tope")
        elif op == "4":
            if pila.ver_tope():
                imprimir_info(f" El ultimo pasajero es: {pila.ver_tope()}")
        elif op == "5":
            numero = leer_entero("Ingrese el numero de pasajero que desea buscar: ")
            if pila.buscar(numero):
                imprimir_exito("Pasajero encontrado")
            else:
                imprimir_error("Pasajero no registrado")
        elif op == "6":
            numero = leer_entero("Ingrese el numero de pasajero que desea modificar: ")
            pasajero = pila.buscar(numero)
            if pasajero is None:
                imprimir_error("No se encontro pasajero ")
            else:
                if confirmar("Desea modificar: "):
                    nuevo_destino = input("Ingrese el nuevo destino: ").strip()
                    nuevo_asiento = input("Ingrese el nuevo asiento: ").strip().upper()
                    pila.modificar(numero, nuevo_destino, nuevo_asiento)
                    imprimir_exito("Pasajero modificado")
                else:
                    imprimir_error("Operacion cancelado")
        elif op == "7":
            numero = leer_entero("Ingrese el numero de pasajero que desea eliminar: ")
            if pila.eliminar_por_numero(numero):
                imprimir_exito("Pasajero eliminado exitosamente.")
            else:
                imprimir_error(f"No se encontró ningún pasajero con el número {numero}.")
        elif op == "8":
            if pila.copiar():
                imprimir_exito("Pasajeros copiados exitosamente")
        elif op == "9":
            if pila.longitud():
                imprimir_exito(f"Tienes {pila.longitud()} pasajeros")
            elif pila.esta_vacia:
                imprimir_error("No tienes pasajero (vacío)")

        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            imprimir_exito("  ✓ Datos de prueba apilados")
        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR

        elif op == "0":
            break
        else:
            imprimir_error("  Opción no válida")
        pausa()

# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente", extras = True)
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                imprimir_exito(" Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            if cola.desencolar():
                imprimir_exito("Pasajero desencolado ")
        elif op == "4":
            if cola.ver_frente():
                imprimir_info(f"Primer pasajero: {cola.ver_frente()}")
        elif op == "5":
            numero = leer_entero("Ingrese el numero de pasajero a buscar:")
            if cola.buscar(numero):
                imprimir_exito("Pasajero encontrado")
            else:
                imprimir_error("Psajero no encontrado")
        elif op == "6":
            numero = leer_entero("Ingrese el nuemro de pasajero a modificar: ")
            pasajero = cola.buscar(numero)
            if pasajero is None: 
                imprimir_error("No se encontro pasajero ")
            else:
                pasajero = input("¿Desea modificar el pasajero: ")
                if pasajero == "si":
                    nuevo_destino = input("Ingrese el nuevo destino: ").strip()
                    nuevo_asiento = input("Ingrese el nuevo asiento: ").strip().upper()
                    cola.modificar(numero, nuevo_destino, nuevo_asiento)
                    imprimir_exito("Pasajero moficado")
                else:
                    imprimir_error("Operacion cancelada")
        elif op == "7":
            numero = leer_entero("Ingrese el numero de pasajero a eliminar: ")
            if cola.buscar(numero):
                cola.eliminar_por_numero(numero)
                imprimir_exito("Pasajero eliminado")
            else:
                imprimir_error("Pasajero no encontrado ")
        elif op == "8":
            if cola.copiar():
                imprimir_exito("Pasajero copiado")
        elif op == "9":
            if cola.longitud():
                imprimir_exito(f"Existen {cola.longitud()} pasajeros")
            elif cola.esta_vacia():
                imprimir_error("No tienes pasajeros (vacio)")
        elif op == "10":
            numero = leer_entero(" Ingrese el número que desea buscar: ")
            pasajero = cola.buscar_binaria(numero)
            if pasajero:
                imprimir_exito(f" Pasajero encontrado: {pasajero}")
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "11":
            cola.ordenar_asc()
            imprimir_exito(" Lista ordenada de forma ascendente")
        elif op == "12":
            cola.ordenar_desc()
            imprimir_exito(" Lista ordenada de forma descendente")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            imprimir_exito("  ✓ Datos de prueba encolados")

        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR

        elif op == "0":
            break
        else:
            imprimir_error("  Opción no válida")
        pausa()


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        imprimir_titulo("  TAREA PILAS Y COLAS · PASAJEROS ✈  ")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()