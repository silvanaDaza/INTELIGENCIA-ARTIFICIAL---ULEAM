def ordenamiento_burbuja(lista):
    """
    Ordena una lista usando el algoritmo de burbuja.

    Args:
        lista: La lista a ordenar.

    Returns:
        La lista ordenada de forma ascendente.
    """

    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

# Ejemplo de uso
mi_lista = [5, 3, 1, 8, 2]
lista_ordenada = ordenamiento_burbuja(mi_lista.copy())  # Evitar modificación de la lista original

print("Lista original:", mi_lista)
print("Lista ordenada:", lista_ordenada)