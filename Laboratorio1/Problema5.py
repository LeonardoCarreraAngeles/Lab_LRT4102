# Importar el módulo random para generar obstáculos de manera aleatoria.
import random
# Definir el tamaño de la matriz (5x5 en este caso).
FILAS = 5
COLUMNAS = 5
# Crear una matriz vacía de 5x5.
matriz = [['o' for _ in range(COLUMNAS)] for _ in range(FILAS)]
# Generar obstáculos de manera aleatoria en la matriz.
# El número de obstáculos será aproximadamente el 20% del total de celdas.
num_obstaculos = int(FILAS * COLUMNAS * 0.2)
for _ in range(num_obstaculos):
    fila = random.randint(0, FILAS - 1)
    columna = random.randint(0, COLUMNAS - 1)
    # Asegurarse de no colocar un obstáculo en la posición inicial (0,0) o final (4,4).
    if (fila == 0 and columna == 0) or (fila == FILAS - 1 and columna == COLUMNAS - 1):
        continue
    matriz[fila][columna] = 'X'  # 'X' representa un obstáculo.
# Función para imprimir la matriz (representada con las x en las líneas anteriores)
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))
    print()
# Función para verificar si una posición es válida (está dentro de la matriz y no es un obstáculo).
def es_valida(fila, columna):
    return 0 <= fila < FILAS and 0 <= columna < COLUMNAS and matriz[fila][columna] == 'o'
# Función principal para mover el robot.
def mover_robot():
    # Posición inicial del robot.
    fila_actual, columna_actual = 0, 0
    # Posición final del robot.
    fila_destino, columna_destino = FILAS - 1, COLUMNAS - 1
    # Dirección inicial del robot (derecha).
    direccion = 'derecha'
    # Lista para almacenar el camino seguido por el robot.
    camino = [(fila_actual, columna_actual)]
    # Matriz para almacenar las flechas del camino.
    flechas = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]

    # Bucle para mover el robot hasta que llegue al destino o no pueda avanzar.
    while (fila_actual != fila_destino or columna_actual != columna_destino):
        # Intentar avanzar en la dirección actual.
        if direccion == 'derecha':
            nueva_fila, nueva_columna = fila_actual, columna_actual + 1
        elif direccion == 'abajo':
            nueva_fila, nueva_columna = fila_actual + 1, columna_actual
        elif direccion == 'izquierda':
            nueva_fila, nueva_columna = fila_actual, columna_actual - 1
        elif direccion == 'arriba':
            nueva_fila, nueva_columna = fila_actual - 1, columna_actual
        # Si la nueva posición es válida, mover el robot.
        if es_valida(nueva_fila, nueva_columna):
            fila_actual, columna_actual = nueva_fila, nueva_columna
            camino.append((fila_actual, columna_actual))
            # Guardar la flecha correspondiente en la matriz de flechas.
            if direccion == 'derecha':
                flechas[fila_actual][columna_actual] = '→'
            elif direccion == 'abajo':
                flechas[fila_actual][columna_actual] = '↓'
            elif direccion == 'izquierda':
                flechas[fila_actual][columna_actual] = '←'
            elif direccion == 'arriba':
                flechas[fila_actual][columna_actual] = '↑'
        else:
            # Si no puede avanzar, girar a la derecha.
            if direccion == 'derecha':
                direccion = 'abajo'
            elif direccion == 'abajo':
                direccion = 'izquierda'
            elif direccion == 'izquierda':
                direccion = 'arriba'
            elif direccion == 'arriba':
                direccion = 'derecha'
        # Si el robot vuelve a la posición inicial, es imposible llegar al destino.
        if (fila_actual == 0 and columna_actual == 0 and len(camino) > 1):
            print("Imposible llegar al destino")
            return
    # Si el robot llega al destino, imprimir los resultados.
    print("Mapa original:")
    imprimir_matriz(matriz)
    print("Camino seguido por el robot:")
    for fila, columna in camino:
        matriz[fila][columna] = '·'  # Marcar el camino en la matriz original.
    imprimir_matriz(matriz)
    print("Ruta con flechas:")
    flechas[0][0] = '·'  # Marcar la posición inicial.
    imprimir_matriz(flechas)

# Llamar a la función principal para mover el robot.
mover_robot()
