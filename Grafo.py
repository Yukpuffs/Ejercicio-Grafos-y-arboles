from collections import deque # Library for queque 

metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Calle 142"],
    "Calle 142":      ["Calle 127"],
    "Calle 127":      ["Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Niza"],
    "Alcalá":         ["Calle 100"],
    "Niza":           ["Calle 100"],
    "Calle 100":      ["Virrey"],
    "Virrey":         ["Centro"],
    "Centro":         ["Portal Sur"],
    "Portal Sur":     ["Centro"],
}

class ruta:
    def __init__(self, grafo):
        self.grafo = grafo

    def ruta_minima(self, origen, destino):

        visitados = set() # Nodes already explored
        cola = deque([[origen]]) #Append stations in a list
        visitados.add(origen)

        while cola:
            camino = cola.popleft()
            nodo = camino[-1]

            for vecino in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]

                    if vecino == destino:
                        return nuevo_camino

                    visitados.add(vecino)
                    cola.append(nuevo_camino)

        return None

rut = ruta(metro)
print("La mejor ruta es: ", rut.ruta_minima("Portal Norte", "Centro"))
