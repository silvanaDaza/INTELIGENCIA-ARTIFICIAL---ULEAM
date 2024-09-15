class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            nodo_actual = self.raiz
            while True:
                if dato < nodo_actual.dato:
                    if nodo_actual.izquierdo is None:
                        nodo_actual.izquierdo = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.izquierdo
                else:
                    if nodo_actual.derecho is None:
                        nodo_actual.derecho = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.derecho

    def buscar(self, dato):
        if self.raiz is None:
            return False
        else:
            nodo_actual = self.raiz
            while True:
                if nodo_actual is None:
                    return False
                if nodo_actual.dato == dato:
                    return True
                elif dato < nodo_actual.dato:
                    nodo_actual = nodo_actual.izquierdo
                else:
                    nodo_actual = nodo_actual.derecho

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(9)

print(arbol.buscar(7))  # Imprime True
print(arbol.buscar(10)) # Imprime False