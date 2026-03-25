
1. Ejercicio

Tu tarea: Implementa una función ruta_minima(grafo, origen, destino) usando BFS que retorne la lista de estaciones del recorrido más corto (menor número de paradas) entre dos estaciones. Si no existe camino, retorna None.

Grafo de prueba:

Python — metro.py (plantilla)
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

# TU SOLUCIÓN AQUÍ:
def ruta_minima(grafo, origen, destino):
    # Pista: usa BFS con seguimiento del camino
    pass

# Prueba:
print(ruta_minima(metro, "Portal Norte", "Centro"))
# Esperado: ['Portal Norte', 'Toberín', 'Calle 142',
#            'Calle 127', 'Alcalá', 'Calle 100', 'Virrey', 'Centro']#
![img](image.png)
