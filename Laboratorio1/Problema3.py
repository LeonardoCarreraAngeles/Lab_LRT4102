# Crear una lista llamada "numeros" que contiene al menos 10 números.
# Estos números pueden ser pares o impares.
numeros = [4, 15, 16, 19, 10, 3, 19, 12, 5, 22]
# Inicializar variables para calcular el promedio de los números pares
# y el producto de los números impares.
suma_pares = 0  # Almacena la suma de los números pares.
contador_pares = 0  # Cuenta cuántos números pares hay.
producto_impares = 1  # Almacena el producto de los números impares (inicia en 1 para multiplicar).
# Recorrer la lista de números para clasificarlos y realizar los cálculos.
for numero in numeros:
    if numero % 2 == 0:  # Si el número es par (divisible entre 2 sin residuo).
        suma_pares += numero  # Sumar el número a la variable suma_pares.
        contador_pares += 1  # Incrementar el contador de números pares.
    else:  # Si el número es impar.
        producto_impares *= numero  # Multiplicar el número a la variable producto_impares.
# Calcular el promedio de los números pares.
# Si no hay números pares, evitamos dividir entre cero.
if contador_pares > 0:
    promedio_pares = suma_pares / contador_pares
else:
    promedio_pares = 0  # Si no hay pares, el promedio es 0.
# Imprimir los resultados.
print(f"El promedio de los números pares es: {promedio_pares}")
print(f"El producto de los números impares es: {producto_impares}")
