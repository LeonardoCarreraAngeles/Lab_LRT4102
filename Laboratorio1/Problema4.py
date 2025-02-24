# Importar el módulo random para generar números aleatorios 
import random
# Generar un número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
# Inicializar variables para contar los intentos del usuario.
intentos = 0  # Contador de intentos.
adivinado = False  # Bandera para saber si el usuario ha adivinado (sirve como nuestro indicador)
print("Tienes que adivinar un número entre 1 y 10")
# Bucle while que continúa hasta que el usuario adivine el número (así también se incrementa el número de intentos)
while not adivinado:
    # Solicitar al usuario que ingrese un número.
    intento = int(input("\nIntroduce tu número: "))
    intentos += 1  # Incrementar el contador de intentos.
    # Comparar el número ingresado con el número secreto.
    if intento < numero_secreto:
        print("El número es demasiado bajo. ¡Intenta de nuevo!")
    elif intento > numero_secreto:
        print("El número es demasiado alto. ¡Intenta de nuevo!")
    else:
        # Si el número es correcto, cambiar la bandera a True.
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
