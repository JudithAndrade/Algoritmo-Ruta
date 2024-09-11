from collections import defaultdict

# Matriz basada en la imagen
matriz = [
    [-3, -3,  2, -3, -2,  1,  2,  0,  0,  2, -2,  0,  1],
    [ 2,  3,  'I', -1, -1, -3, -2, -3, -3, -2, -2, 0, 1],
    [ 1, -3, -3,  2,  3,  1, -3,  2,  1, -2, -3, -2,  3],
    [ 0,  0,  3,  0,  3, -3, -2, -3, -3,  0,  2,  1,  1],
    [ 2, -1, -1, -3, -3,  3,  0, -3,  1, -2, -3,  0,  1],
    [ 0,  3, -1,  1,  1, -2,  2, -2,  2,  1, -3,  0,  0],
    [ 0,  3,  2,  0,  1,  1,  2,  3, -1, -3,  0,  0, -2],
    [ 3,  3, -3, -3, -2,  3, -3,  1, -3, -3, -2, -2, -1],
    [-2, -2,  1,  0,  1,  0,  0,  0,  0,  2, -3,  1,  0],
    [-3, -3,  0, -1, -3,  1,  2,  3, -2,  1,  1,  0,  0],
    [-1,  0,  1,  2,  1,  0, 'F',  0,  1,  0,  3, -1, 3],
    [ 1, -3,  1,  0,  1,  2,  1,  2,  1,  3,  1,  3,  1],
]

# Dimensiones de la matriz
filas = len(matriz)
columnas = len(matriz[0])

# Posiciones de "I" y "F"
inicio = (1, 2)
fin = (10, 6)

# Movimientos posibles: derecha, abajo, izquierda, arriba
movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Función para verificar si una posición es válida
def es_valida(x, y):
    return 0 <= x < filas and 0 <= y < columnas

# Memoización para guardar los costos mínimos y máximos desde cada celda
memo_min = defaultdict(lambda: float('inf'))
memo_max = defaultdict(lambda: float('-inf'))

# Función DFS para encontrar la ruta con menor y mayor costo
def dfs(x, y, costo_actual, visitado):
    # Si llegamos a "F"
    if (x, y) == fin:
        return costo_actual, costo_actual
    
    # Si ya hemos calculado los costos para esta celda
    if (x, y) in memo_min:
        return memo_min[(x, y)], memo_max[(x, y)]
    
    # Marcar la celda actual como visitada
    visitado.add((x, y))
    
    min_costo = float('inf')
    max_costo = float('-inf')
    
    # Explorar las direcciones posibles
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valida(nx, ny) and (nx, ny) not in visitado:
            # Sumar el valor de la celda en la matriz si es un entero
            nuevo_costo = costo_actual
            if isinstance(matriz[nx][ny], int):
                nuevo_costo += matriz[nx][ny]
            
            # Recursión DFS para encontrar el costo mínimo y máximo desde el nuevo punto
            costo_min, costo_max = dfs(nx, ny, nuevo_costo, visitado)
            
            # Actualizar el costo mínimo y máximo encontrado
            min_costo = min(min_costo, costo_min)
            max_costo = max(max_costo, costo_max)
    
    # Desmarcar la celda actual para permitir otras rutas
    visitado.remove((x, y))
    
    # Guardar los resultados en la memoización
    memo_min[(x, y)] = min_costo
    memo_max[(x, y)] = max_costo
    
    return min_costo, max_costo

# Ejecutar DFS desde el punto "I"
costo_minimo, costo_maximo = dfs(inicio[0], inicio[1], 0, set())

# Imprimir los resultados con el contexto de los puntos "I" y "F"
print(f"Desde el punto de inicio 'I' en {inicio} hasta el punto 'F' en {fin}:")
print(f"El costo de la ruta más barata es: {costo_minimo}")
print(f"El costo de la ruta más cara es: {costo_maximo}")
