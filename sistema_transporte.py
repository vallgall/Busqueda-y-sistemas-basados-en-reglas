# Definición de las conexiones entre estaciones
conexiones = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# Implementación del algoritmo BFS
from collections import deque

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        elif node not in visited:
            for adjacent in conexiones.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.add(node)
    return None

# Interfaz de usuario
def main():
    inicio = input("Ingrese la estación de inicio: ").upper()
    fin = input("Ingrese la estación de destino: ").upper()
    ruta = bfs(inicio, fin)
    if ruta:
        print(f"La mejor ruta es: {' -> '.join(ruta)}")
    else:
        print("No se encontró una ruta.")

if __name__ == "__main__":
    main()
