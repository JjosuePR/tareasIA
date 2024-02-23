class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None

    def _insertar_recursivo(self, nodo, nombre):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre)
            else:
                self._insertar_recursivo(nodo.derecha, nombre)

    def insertar(self, nombre):
        if self.raiz is None:
            self.raiz = Nodo(nombre)
        else:
            self._insertar_recursivo(self.raiz, nombre)

    def _buscar_nodo_recursivo(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self._buscar_nodo_recursivo(nodo.izquierda, nombre)
        return self._buscar_nodo_recursivo(nodo.derecha, nombre)

    def buscarNodo(self, nombre):
        return self._buscar_nodo_recursivo(self.raiz, nombre)

    def _imprimir_arbol_recursivo(self, nodo):
        if nodo:
            self._imprimir_arbol_recursivo(nodo.izquierda)
            print(nodo.nombre)
            self._imprimir_arbol_recursivo(nodo.derecha)

    def imprimirArbol(self):
        self._imprimir_arbol_recursivo(self.raiz)

# Ejemplo de uso
if __name__ == "__main__":
    arbol = Arbol()
    nombres = ["Juan", "Ana", "Pedro", "Luis", "Maria"]
    
    for nombre in nombres:
        arbol.insertar(nombre)
    
    print("Árbol binario de búsqueda:")
    arbol.imprimirArbol()

    nombre_buscar = "Pedro"
    nodo_encontrado = arbol.buscarNodo(nombre_buscar)
    
    if nodo_encontrado:
        print(f"Encontrado nodo con nombre '{nombre_buscar}'")
    else:
        print(f"Nodo con nombre '{nombre_buscar}' no encontrado")
