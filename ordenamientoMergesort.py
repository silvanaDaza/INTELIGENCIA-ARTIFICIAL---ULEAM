def merge(lista_izquierda, lista_derecha):
    """
    Combina dos listas ordenadas en una sola lista ordenada.

    Args:
        lista_izquierda: La primera lista ordenada.
        lista_derecha: La segunda lista ordenada.

    Returns:
        La lista combinada ordenada de forma ascendente.
    """

    lista_combinada = []
    i = 0
    j = 0
    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] <= lista_derecha[j]:
            lista_combinada.append(lista_izquierda[i])
            i += 1
        else:
            lista_combinada.append(lista_derecha[j])
            j += 1

    # Agregar elementos restantes
    lista_combinada.extend(lista_izquierda[i:])
    lista_combinada.extend(lista_derecha[j:])

    return lista_combinada

def ordenamiento_mergesort(lista):
    """
    Ordena una lista usando el algoritmo mergesort.

    Args:
        lista: La lista a ordenar.

    Returns:
        La lista ordenada de forma ascendente.
    """

    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    lista_izquierda = ordenamiento_mergesort(lista[:mitad])
    lista_derecha = ordenamiento_mergesort(lista[mitad:])

    return merge(lista_izquierda, lista_derecha)

# Ejemplo de uso
mi_lista = [5, 3, 1, 8, 2]
lista_ordenada = ordenamiento_mergesort(mi_lista.copy())  # Evitar modificación de la lista original

print("Lista original:", mi_lista)
print("Lista ordenada:", lista_ordenada)