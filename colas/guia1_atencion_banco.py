from collections import deque

cola = deque()

while True:
    print("\n1.Llega cliente 2.Atender 3.Ver frente 4.Ver toda la cola 5.Clientes VIp 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)
        print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}.")

    elif op == "3":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "4":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " ← siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")
    elif op == "5":
        nom = input("Nombre: ")
        cola.appendleft(nom)
        print(f"Cliente VIP tiene prioridad: {nom} entro en la fila  ")
    elif op == "6":
        break