def ordenamiento_insercion(lista):
    """
    Ordena una lista usando el algoritmo de inserción.

    Args:
        lista: La lista a ordenar.

    Returns:
        La lista ordenada de forma ascendente.
    """

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual

    return lista

# Ejemplo de uso
mi_lista = [5, 3, 1, 8, 2]
lista_ordenada = ordenamiento_insercion(mi_lista.copy())  # Evitar modificación de la lista original

print("Lista original:", mi_lista)
print("Lista ordenada:", lista_ordenada)