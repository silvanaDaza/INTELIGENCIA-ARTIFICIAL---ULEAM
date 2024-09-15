class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)  # Para grafos no dirigidos

    def imprimir_grafo(self):
        for nodo, vecinos in self.grafo.items():
            print(nodo, "->", vecinos)

# Ejemplo de uso:
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 3)

g.imprimir_grafo()