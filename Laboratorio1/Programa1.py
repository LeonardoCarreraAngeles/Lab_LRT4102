# Pedir al usuario que ingrese un número entero positivo
n = int(input("Introduce un número entero positivo: "))
# Verificar si el número ingresado es válido (mayor que 0)
if n <= 0:
    # Si no es válido, mostrar un mensaje de error
    print("El número debe ser positivo. Intenta de nuevo.")
else:
    # Calcular la suma de los números desde 1 hasta n usando la fórmula matemática
    suma = n * (n + 1) // 2
    # Mostrar el resultado al usuario
    print(f"La suma de los números enteros es: {suma}")
