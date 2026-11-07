from collections import deque

def paren_balanceado(s):
    pila = deque()
    nueva_pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}   # cierre → apertura

    for i, ch in enumerate(s):
        if ch in "([{":
            # Es apertura, la apilo
            pila.append(ch)
            nueva_pila.append(i)
        elif ch in ")]}":
            # Es cierre, tope debe ser su pareja
            if not pila or pila.pop() != parejas[ch]:
                pos_error = nueva_pila.pop() if nueva_pila else i
                return f"Error en pos {i}: no combina con lo abierto en pos {pos_error}"

    # Al final: si sobra algo en la pila, hay aperturas sin cerrar
    if len(pila) == 0 :
        return True 
    else:
        return f"Error en: {nueva_pila.pop()} nunca se cerro"


# Pruebas
tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]
for t in tests:
    print(f"{t!r:15} → {paren_balanceado(t)}")