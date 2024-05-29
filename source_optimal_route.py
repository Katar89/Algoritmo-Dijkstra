import heapq

class Grafo:
    def __init__(self): # Inicializa un grafo vacío
        self.vertices = {}

    def agregar_arista(self, origen, destino, peso): # Añade una arista entre origen y destino con un peso dado.
        if origen not in self.vertices:
            self.vertices[origen] = []
        if destino not in self.vertices:    
            self.vertices[destino] = []
        self.vertices[origen].append((destino, peso)) # La arista se añade en ambas direcciones para representar un grafo no dirigido.
        self.vertices[destino].append((origen, peso)) 

    def __str__(self):
        return str(self.vertices) # Devuelve cadena con los nodos
    
def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo.vertices} # Inicializa todas las distancias a infinito y la distancia del nodo de inicio a 0.
    distancias[inicio] = 0
    prioridad = [(0, inicio)]
    predecesores = {nodo: None for nodo in grafo.vertices}
    
    while prioridad:
        distancia_actual, nodo_actual = heapq.heappop(prioridad) # Usa una fila de prioridad para explorar los nodos, comenzando por el nodo de inicio.
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo.vertices[nodo_actual]:
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]: # Almacena los predecesores para poder reconstruir el camino más corto.
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(prioridad, (distancia, vecino)) # Mueve el item a la ilera
                
    return distancias, predecesores

def reconstruir_camino(predecesores, inicio, fin):
    camino = []
    nodo_actual = fin  # Nodo destino
    while nodo_actual:
        camino.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual] # Se regresa por donde encontro el camino de menos costo
    camino.reverse()
    return camino

def calcular_peso_total(camino, grafo):
    peso_total = 0
    for i in range(len(camino) - 1): # Se resta una unidad para obedecer el orden de indices (0, 1, 2, 3)
        origen = camino[i]
        destino = camino[i + 1]
        for vecino, peso in grafo.vertices[origen]:
            if vecino == destino:
                peso_total += peso # Cada iteracion del ciclo suma su respectivo peso por nodo recorrido
                break
    return peso_total

#----------------------------- FUNCION MAIN -----------------------------

def main():
    grafo = Grafo() 
    grafo.agregar_arista('A', 'B', 1) 
    grafo.agregar_arista('B', 'C', 2)
    grafo.agregar_arista('A', 'C', 4)
    grafo.agregar_arista('C', 'D', 1)
    grafo.agregar_arista('B', 'D', 5)
    # grafo.agregar_arista('D', 'C', 3 ) ---- (Nodo inicial, Nodo final, Peso de la operacion)


    inicio = input("Ingrese el nodo de inicio: ").strip()  # NODO DE INICIO
    fin = input("Ingrese el nodo de finalización: ").strip() # NODO DE FINALIZACION 
    
    distancias, predecesores = dijkstra(grafo, inicio)
    camino = reconstruir_camino(predecesores, inicio, fin)
    peso_total = calcular_peso_total(camino, grafo)
    
    print(f"Distancia más corta desde {inicio} hasta {fin}: {distancias[fin]} nodos")
    print(f"Camino: {' -> '.join(camino)}")
    print(f"Costo total: {peso_total}")


main()
