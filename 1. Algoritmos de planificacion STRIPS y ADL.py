from pyhop import *

# Definir el estado inicial
estado_inicial = State("estado_inicial")
estado_inicial.pilasobre = {'A': 'mesa', 'B': 'mesa', 'C': 'mesa'}

# Definir el estado objetivo
estado_objetivo = State("estado_objetivo")
estado_objetivo.pilasobre = {'A': 'B', 'B': 'C', 'C': 'mesa'}

# Definir las acciones disponibles
def mover(bloque, desde, hacia):
    if desde != "mesa" and estado_inicial.pilasobre[bloque] == desde and estado_inicial.pilasobre[hacia] == "mesa":
        return [('mover', bloque, desde, hacia)]

def apilar(bloque, sobre, hacia):
    if estado_inicial.pilasobre[bloque] == sobre and estado_inicial.pilasobre[hacia] == "mesa":
        return [('apilar', bloque, sobre, hacia)]

# Registrar las acciones y los métodos
declare_operators(mover, apilar)
declare_methods('mover', 'apilar')

# Resolver el problema de planificación
problema = Problem(estado_inicial, [('mover', 'A', 'mesa', 'B'), ('mover', 'B', 'mesa', 'C')], estado_objetivo)
solucion = pyhop(problema, verbose=2)

# Imprimir el plan encontrado
for accion in solucion:
    print(accion)
