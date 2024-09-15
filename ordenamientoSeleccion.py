def ordenamiento_seleccion(lista):
    """
    Ordena una lista usando el algoritmo de selección.

    Args:
        lista: La lista a ordenar.

    Returns:
        La lista ordenada de forma ascendente.
    """

    for i in range(len(lista)):
        min_indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        lista[i], lista[min_indice] = lista[min_indice], lista[i]

    return lista

# Ejemplo de uso
mi_lista = [5, 3, 1, 8, 2]
lista_ordenada = ordenamiento_seleccion(mi_lista.copy())  # Evitar modificación de la lista original

print("Lista original:", mi_lista)
print("Lista ordenada:", lista_ordenada)