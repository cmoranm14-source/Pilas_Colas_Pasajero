from collections import deque

def procesar_impresora(trabajos):
    cola = deque(trabajos)
    tiempo_total = 0
    cancelar = input("Nombre del archivo a cancelar (Enter para ninguno): ")
    if cancelar:
        for nombre, paginas in cola:
            if nombre == cancelar:
                cola.remove((nombre, paginas))
                print(f"Cancelado {cancelar}")
    while cola:
        nombre, paginas = cola.popleft()      # FIFO: el primero en llegar
        tiempo = paginas * 2
        tiempo_total += tiempo
        print(f"Imprimiendo {nombre}: {paginas} páginas → {tiempo}s "
              f"(acumulado {tiempo_total}s)")

    return tiempo_total

# --- Uso ---
trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10),
]

total = procesar_impresora(trabajos)
print(f"\nTiempo total: {total}s")