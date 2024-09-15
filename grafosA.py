import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = {}
        self.grafo[nodo1][nodo2] = peso

    def a_estrella(self, nodo_inicial, nodo_final, heuristica):
        """
        Implementa el algoritmo A*.

        Args:
            nodo_inicial: El nodo de inicio.
            nodo_final: El nodo de destino.
            heuristica: Una función que estima la distancia al nodo final.

        Returns:
            Un diccionario con las distancias más cortas y los nodos padres.
        """

        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[nodo_inicial] = 0
        padre = {}
        cola_prioridad = [(0, nodo_inicial)]

        while cola_prioridad:
            (costo_actual, nodo_actual) = heapq.heappop(cola_prioridad)

            if nodo_actual == nodo_final:
                break

            for vecino, peso in self.grafo[nodo_actual].items():
                nuevo_costo = distancias[nodo_actual] + peso
                if nuevo_costo < distancias[vecino]:
                    distancias[vecino] = nuevo_costo
                    padre[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nuevo_costo + heuristica(vecino, nodo_final), vecino))

        return distancias, padre

# Ejemplo de uso
def heuristica_manhattan(nodo, nodo_final):
    # Heurística de Manhattan (distancia en línea recta)
    # Ajusta esta función según tu problema específico
    x1, y1 = nodo
    x2, y2 = nodo_final
    return abs(x1 - x2) + abs(y1 - y2)

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 10)
grafo.agregar_arista('A', 'C', 15)
grafo.agregar_arista('B', 'C', 5)
grafo.agregar_arista('B', 'D', 12)
grafo.agregar_arista('C', 'D', 2)
grafo.agregar_arista('C', 'E', 5)
grafo.agregar_arista('D', 'E', 5)

# Encontrar el camino más corto desde 'A' a 'E'
distancias, padres = grafo.a_estrella('A', 'E', heuristica_manhattan)

# Reconstruir el camino
camino = []
nodo_actual = 'E'
while nodo_actual:
    camino.insert(0, nodo_actual)
    nodo_actual = padres.get(nodo_actual)

print("Camino más corto:", camino)
print("Distancia total:", distancias['E'])