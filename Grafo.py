from collections import deque # Library for queque 

metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Portal Norte", "Calle 142"],
    "Calle 142":      ["Toberín", "Calle 127"],
    "Calle 127":      ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Calle 127", "Niza"],
    "Alcalá":         ["Calle 127", "Calle 100"],
    "Niza":           ["Pepe Sierra", "Calle 100"],
    "Calle 100":      ["Alcalá", "Niza", "Virrey"],
    "Virrey":         ["Calle 100", "Centro"],
    "Centro":         ["Virrey", "Portal Sur"],
    "Portal Sur":     ["Centro"],
}

class ruta:

    def ruta_minima(grafo, origen, destino):
        
        visitados = set() # Nodes already explored
        cola = deque([[origen]]) #Append stations in a list
        visitados.add(origen)

        while cola:
            camino = cola.popleft()
            nodo = camino[-1]

            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]

                    if vecino == destino:
                        return nuevo_camino

                    visitados.add(vecino)
                    cola.append(nuevo_camino)

        return None

print("La mejor ruta es: ", ruta.ruta_minima(metro, "Portal Norte", "Centro"))
