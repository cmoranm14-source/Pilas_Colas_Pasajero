from collections import deque

historial = deque()

while True:
    print("\n1.Hacer 2.Deshacer 3.Ver historial 4.Salir")
    op = input("Opción: ")

    if op == "1":
        accion = input("Descripción: ")
        historial.append(accion)
        print(f"Hecho: {accion}")

    elif op == "2":
        if not historial:
            print("Nada que deshacer")
        else:
            deshecha = historial.pop()
            print(f"Deshecho: {deshecha}")

    elif op == "3":
        if not historial:
            print("(vacío)")
        else:
            for i, a in enumerate(historial):
                print(f"  {i+1}. {a}")

    elif op == "4":
        break