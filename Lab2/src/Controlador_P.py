import turtle
import time
import math

# Configuración de la pantalla. Se establece el tamaño de la ventana.
screen = turtle.Screen()
screen.setup(width=600, height=600)
# Configuración de la tortuga. Se define la forma, color, tamaño de pluma y velocidad.
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("blue")
turtle.pensize(5)
turtle.speed(1)
# Parámetros de la estrella.  Define el número de puntas y el radio.
num_puntas = 5
radio = 100
# Ganancia proporcional (Kp).  Ajusta la velocidad del controlador.
kp = 0.1
def controlador_p(x_actual, y_actual, objetivo_x, objetivo_y, kp):
    """Calcula las velocidades en x e y basándose en un controlador proporcional."""
    # Calcula el error en x e y.  Diferencia entre la posición actual y el objetivo.
    error_x = objetivo_x - x_actual
    error_y = objetivo_y - y_actual
    # Calcula la velocidad en x e y.  Proporcional al error.
    velocidad_x = kp * error_x
    velocidad_y = kp * error_y
    return velocidad_x, velocidad_y
# Calcula las coordenadas de los vértices de la estrella.  Guarda las coordenadas en una lista.
vertices = []
angulo = -math.pi / 2  # Ángulo inicial, apuntando hacia arriba.
for i in range(num_puntas):
    # Calcula las coordenadas x e y de cada vértice. Usa trigonometría.
    x = radio * math.cos(angulo)
    y = radio * math.sin(angulo)
    vertices.append((x, y))
    angulo += 4 * math.pi / num_puntas  # Incrementa el ángulo para el siguiente vértice.
# Agrega el primer vértice al final para cerrar la estrella.  Completa la figura.
vertices.append(vertices[0])
# Bucle principal para dibujar la estrella. Itera sobre cada vértice.
for vertice in vertices:
    # Obtiene las coordenadas del vértice objetivo.
    objetivo_x, objetivo_y = vertice
    while True:
        # Obtiene la posición actual de la tortuga.
        x_actual, y_actual = turtle.position()
        # Calcula las velocidades con el controlador P.  Llama a la función del controlador.
        velocidad_x, velocidad_y = controlador_p(x_actual, y_actual, objetivo_x, objetivo_y, kp)
        # Mueve la tortuga.  Ajusta la dirección y avanza.
        turtle.setheading(turtle.towards(objetivo_x, objetivo_y))
        turtle.forward(abs(velocidad_x) + abs(velocidad_y))
        # Condición de parada.  Verifica si la tortuga llegó al objetivo.
        distancia_al_objetivo = turtle.distance(objetivo_x, objetivo_y)
        if distancia_al_objetivo < 1:
            break
        time.sleep(0.03)  # Pequeña pausa. Controla la velocidad de la animación.

turtle.done()
