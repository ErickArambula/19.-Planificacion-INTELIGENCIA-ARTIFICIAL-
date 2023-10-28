# Definir el espacio de estados como un conjunto de posiciones (x, y)
estados = set()
for x in range(4):  # Rango de 0 a 3 en el eje x
    for y in range(4):  # Rango de 0 a 3 en el eje y
        estados.add((x, y))

# Definir los operadores para mover el robot
def mover_arriba(estado):
    x, y = estado
    if y < 3:
        return (x, y + 1)

def mover_abajo(estado):
    x, y = estado
    if y > 0:
        return (x, y - 1)

def mover_izquierda(estado):
    x, y = estado
    if x > 0:
        return (x - 1, y)

def mover_derecha(estado):
    x, y = estado
    if x < 3:
        return (x + 1, y)

# Ejemplo de uso de los operadores
estado_actual = (0, 0)
nuevo_estado = mover_arriba(estado_actual)
print(f"Estado actual: {estado_actual}, Nuevo estado: {nuevo_estado}")
