def invertir_con_pila(s):
    pila = []
    palabras = s.split()
    for palabra in palabras:
        pila.append(palabra)

    resultado = ""
    while pila:
        if resultado != "":
            resultado += " "
        resultado += pila.pop()
    return resultado


print(invertir_con_pila("Python automatizacion"))    # nohtyP
print(invertir_con_pila("Hola Mundo"))