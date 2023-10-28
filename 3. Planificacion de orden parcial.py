from pyhop import *

# Definir el estado inicial
estado_inicial = State("estado_inicial")
estado_inicial.lugar = 'casa'
estado_inicial.musica = 'apagada'
estado_inicial.decoracion = 'ninguna'
estado_inicial.comida = 'pizza'
estado_inicial.bebida = 'refrescos'

# Definir el estado objetivo
estado_objetivo = State("estado_objetivo")
estado_objetivo.lugar = 'jardín'
estado_objetivo.musica = 'encendida'
estado_objetivo.decoracion = 'luces'
estado_objetivo.comida = 'barbacoa'
estado_objetivo.bebida = 'cerveza'

# Definir las acciones disponibles
def cambiar_lugar(estado, lugar):
    return [('cambiar_lugar',), (estado, 'lugar', lugar)]

def encender_musica(estado):
    return [('encender_musica',), (estado, 'musica', 'encendida')]

def poner_decoracion(estado, decoracion):
    return [('poner_decoracion',), (estado, 'decoracion', decoracion)]

def cambiar_comida(estado, comida):
    return [('cambiar_comida',), (estado, 'comida', comida)]

def cambiar_bebida(estado, bebida):
    return [('cambiar_bebida',), (estado, 'bebida', bebida)]

# Registrar las acciones
declare_operators(cambiar_lugar, encender_musica, poner_decoracion, cambiar_comida, cambiar_bebida)

# Resolver el problema de planificación de orden parcial
problema = Problem(estado_inicial, [
    (cambiar_lugar, 'jardín'),
    (poner_decoracion, 'luces'),
    (encender_musica,),
    (cambiar_comida, 'barbacoa'),
    (cambiar_bebida, 'cerveza')
], estado_objetivo)

solucion = pyhop(problema, verbose=2)

# Imprimir el plan encontrado
for accion in solucion:
    print(accion)
