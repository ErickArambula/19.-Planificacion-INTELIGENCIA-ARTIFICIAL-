from pyhop import *

# Declaración de las acciones y precondiciones
def mover(estado, robot, origen, destino):
    if estado["en"][robot] == origen:
        return [('en', robot, destino)]

def revisar_entorno(estado, robot, sala):
    if sala == "sala1":
        return [('condicion', 'normal')]
    elif sala == "sala2":
        return [('condicion', 'anomalia')]

# Inicialización de las acciones y precondiciones
declare_actions('mover', mover)
declare_actions('revisar_entorno', revisar_entorno)

# Definición del estado inicial
initial_state = State('estado_inicial')
initial_state["en"] = {"robot1": "sala1"}
initial_state["condicion"] = "normal"

# Definición del estado objetivo
goal_state = State('estado_objetivo')
goal_state["en"] = {"robot1": "sala2"}

# Plan original
plan = pyhop(initial_state, [('mover', 'robot1', 'sala1', 'sala2')], verbose=3)
print("Plan original:", plan)

# Durante la ejecución, revisión del entorno
estado_actual = update_state(initial_state, plan)
nueva_condicion = revisar_entorno(estado_actual, 'robot1', 'sala2')

if nueva_condicion:
    print("Se detectó una anomalía en el entorno. Replanificación...")
    plan_actualizado = pyhop(estado_actual, [('mover', 'robot1', 'sala1', 'sala2')], verbose=3)
    print("Plan actualizado:", plan_actualizado)
