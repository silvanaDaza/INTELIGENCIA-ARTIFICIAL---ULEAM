def busqueda_binaria(lista, valor_buscado):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Args:
        lista: La lista ordenada donde se realizará la búsqueda.
        valor_buscado: El valor a buscar.

    Returns:
        El índice del valor si se encuentra, -1 si no se encuentra.
    """

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor_buscado:
            return medio
        elif lista[medio] < valor_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1