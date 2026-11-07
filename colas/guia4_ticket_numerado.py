from collections import deque

cola = deque()
proximo = 1

while True:
    print("\n1.Llega 2.Atender 3.Ver cola 4.Salir")
    op = input("Opción: ")

    if op == "1":
        cola.append(proximo)
        print(f"Ticket {proximo} asignado. {len(cola)} en espera.")
        proximo += 1
    elif op == "2":
        if not cola:
            print("Sin clientes")
        else:
            print(f"Turno {cola.popleft()}")
    elif op == "3":
        print(list(cola))
    elif op == "4":
        break