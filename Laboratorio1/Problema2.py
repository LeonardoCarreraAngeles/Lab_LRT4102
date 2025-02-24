# Lista de operadores con sus datos: nombre, sueldo por hora y horas trabajadas.
# Cada operador está representado como un diccionario dentro de la lista.
operadores = [
    {"nombre": "Cesar", "sueldo_hora": 15, "horas_trabajadas": 40},
    {"nombre": "Leonardo", "sueldo_hora": 20, "horas_trabajadas": 35},
    {"nombre": "Pedro", "sueldo_hora": 18, "horas_trabajadas": 45},
    {"nombre": "Daniela", "sueldo_hora": 22, "horas_trabajadas": 38},
    {"nombre": "Jorge", "sueldo_hora": 17, "horas_trabajadas": 42},
    {"nombre": "Stephannie", "sueldo_hora": 19, "horas_trabajadas": 37},
]
# Función para calcular la paga de un operador.
# Recibe el sueldo por hora y las horas trabajadas, y retorna el total a pagar.
def calcular_paga(sueldo_hora, horas_trabajadas):
    return sueldo_hora * horas_trabajadas
# Mostrar la paga de cada operador.
# Recorremos la lista de operadores y calculamos la paga para cada uno.
print("Pagos de los operadores:")
for operador in operadores:
    # Extraemos los datos del operador actual.
    nombre = operador["nombre"]
    sueldo_hora = operador["sueldo_hora"]
    horas_trabajadas = operador["horas_trabajadas"]
    # Calculamos la paga usando la función definida anteriormente.
    paga = calcular_paga(sueldo_hora, horas_trabajadas)
    # Mostramos el nombre del operador y su paga correspondiente.
    print(f"{nombre}: ${paga}")
# Pedir al usuario que ingrese sus horas trabajadas y el costo por hora.
# Usamos float para permitir valores decimales, como 37.5 horas.
horas = float(input("\nIntroduce las horas trabajadas: "))
costo_hora = float(input("Introduce el costo por hora: "))
# Calcular la paga del usuario multiplicando las horas por el costo por hora.
paga_usuario = horas * costo_hora
# Mostrar la paga que le corresponde al usuario.
print(f"La paga que te corresponde es: ${paga_usuario}")
