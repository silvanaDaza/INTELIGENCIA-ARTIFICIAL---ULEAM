def busqueda_lineal(lista, valor_buscado):

    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1

# Ejemplo de uso:
mi_lista = [3, 7, 1, 9, 5]
valor = 7
indice = busqueda_lineal(mi_lista, valor)

if indice != -1:
    print("El valor", valor, "se encontro en el indice", indice)
else:
    print("El valor", valor, "no se encontro en la lista")