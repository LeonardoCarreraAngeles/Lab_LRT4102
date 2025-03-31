import turtle
import time
import math
import csv

# Configuración de la pantalla. Se establece el tamaño de la ventana.
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Configuración de la tortuga. Se define la forma, color, tamaño de pluma y velocidad.
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("blue")
turtle.pensize(5)
turtle.speed(1)

# Parámetros de la estrella. Define el número de puntas y el radio.
num_puntas = 5
radio = 100

# Ganancias del controlador PI. Ajusta la velocidad y la precisión.
kp = 0.1  # Ganancia proporcional
ki = 0.001 # Ganancia integral

# Variables para el error acumulado. Se usan para el término integral.
error_acumulado_x = 0
error_acumulado_y = 0

# Delta tiempo, para el cálculo de la integral
dt = 0.03

def controlador_pi(x_actual, y_actual, objetivo_x, objetivo_y, kp, ki):
    """Calcula las velocidades en x e y basándose en un controlador PI."""

    # Calcula el error en x e y. Diferencia entre la posición actual y el objetivo.
    error_x = objetivo_x - x_actual
    error_y = objetivo_y - y_actual

    # Acumula el error para el término integral.
    global error_acumulado_x, error_acumulado_y
    error_acumulado_x += error_x * dt # Se multiplica por dt para la integración
    error_acumulado_y += error_y * dt

    # Calcula la velocidad en x e y.  Combina los términos proporcional e integral.
    velocidad_x = kp * error_x + ki * error_acumulado_x
    velocidad_y = kp * error_y + ki * error_acumulado_y

    return velocidad_x, velocidad_y

# Calcula las coordenadas de los vértices de la estrella. Guarda las coordenadas en una lista.
vertices = []
angulo = -math.pi / 2  # Ángulo inicial, apuntando hacia arriba.
for i in range(num_puntas):
    # Calcula las coordenadas x e y de cada vértice. Usa trigonometría.
    x = radio * math.cos(angulo)
    y = radio * math.sin(angulo)
    vertices.append((x, y))
    angulo += 4 * math.pi / num_puntas  # Incrementa el ángulo para el siguiente vértice.

# Agrega el primer vértice al final para cerrar la estrella. Completa la figura.
vertices.append(vertices[0])

# Listas para almacenar los datos de tiempo y error
tiempos = []
errores = []
tiempo_actual = 0


# Bucle principal para dibujar la estrella. Itera sobre cada vértice.
for vertice in vertices:
    # Obtiene las coordenadas del vértice objetivo.
    objetivo_x, objetivo_y = vertice
    while True:
        # Obtiene la posición actual de la tortuga.
        x_actual, y_actual = turtle.position()

        # Calcula las velocidades con el controlador PI. Llama a la función del controlador.
        velocidad_x, velocidad_y = controlador_pi(x_actual, y_actual, objetivo_x, objetivo_y, kp, ki)

        # Mueve la tortuga. Ajusta la dirección y avanza.
        turtle.setheading(turtle.towards(objetivo_x, objetivo_y))
        turtle.forward(abs(velocidad_x) + abs(velocidad_y))

        # Condición de parada. Verifica si la tortuga llegó al objetivo.
        distancia_al_objetivo = turtle.distance(objetivo_x, objetivo_y)

        # Registrar datos
        tiempos.append(tiempo_actual)
        errores.append(distancia_al_objetivo)
        tiempo_actual += dt


        if distancia_al_objetivo < 1:
            break

        time.sleep(dt)  # Pequeña pausa. Controla la velocidad de la animación.
# Guardar los datos en un archivo CSV
with open("datos_pi.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Tiempo", "Error"])  # Encabezado
    for tiempo, error in zip(tiempos, errores):
        escritor_csv.writerow([tiempo, error])

turtle.done() # Mantiene la ventana abierta hasta que se cierra manualmente.
