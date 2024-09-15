class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        self.grafo[nodo1].append(nodo2)

    def dfs(self, nodo_inicial, visitados=None):
        """
        Realiza una búsqueda en profundidad en un grafo.

        Args:
            nodo_inicial: El nodo desde donde iniciar la búsqueda.
            visitados (opcional): Un conjunto para rastrear los nodos visitados.

        Returns:
            Una lista con el recorrido del DFS.
        """

        if visitados is None:
            visitados = set()
        visitados.add(nodo_inicial)
        recorrido = [nodo_inicial]

        for vecino in self.grafo.get(nodo_inicial, []):
            if vecino not in visitados:
                recorrido.extend(self.dfs(vecino, visitados.copy()))

        return recorrido

# Ejemplo de uso
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 0)
g.agregar_arista(2, 3)
g.agregar_arista(3, 3)

recorrido_dfs = g.dfs(0)

print("Recorrido DFS:", recorrido_dfs)