from pyhop import *
import random

# Declaración de las acciones y precondiciones
def cargar_camion(estado, camion, paquete, destino):
    if estado["en_camion"][paquete] == "none" and estado["en"][paquete] == "almacen" and estado["en_camion"][camion] == "none" and estado["en"][camion] == "almacen":
        return [('en_camion', paquete, camion), ('en', paquete, destino)]
    return []

def descargar_camion(estado, camion, paquete, destino):
    if estado["en_camion"][paquete] == camion and estado["en_camion"][camion] == "none" and estado["en"][paquete] == destino:
        return [('en_camion', paquete, "none"), ('en', paquete, destino)]
    return []

# Inicialización de las acciones y precondiciones
declare_actions('cargar_camion', cargar_camion)
declare_actions('descargar_camion', descargar_camion)

# Definición del estado inicial
initial_state = State('estado_inicial')
initial_state["en_camion"] = {"paqueteA": "none", "paqueteB": "none"}
initial_state["en"] = {"paqueteA": "almacen", "paqueteB": "almacen", "camion1": "almacen"}
initial_state["en_camion"] = {"camion1": "none"}

# Definición del estado objetivo
goal_state = State('estado_objetivo')
goal_state["en_camion"] = {"paqueteA": "camion1"}
goal_state["en"] = {"paqueteA": "destino1", "paqueteB": "almacen", "camion1": "destino1"}
goal_state["en_camion"] = {"camion1": "none"}

# Resolución del problema de planificación
plan = pyhop(initial_state, [('cargar_camion', 'paqueteA', 'camion1', 'destino1')], verbose=3)
print(plan)
