from heapq import heappush, heappop

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = {}
        self.grafo[nodo1][nodo2] = peso

    def dijkstra(self, nodo_inicial):
        """
        Implementa el algoritmo de Dijkstra para encontrar las distancias más cortas.

        Args:
            nodo_inicial: El nodo desde donde iniciar el cálculo.

        Returns:
            Un diccionario con las distancias más cortas de nodo