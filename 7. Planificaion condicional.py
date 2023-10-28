from pyhop import *

# Declaración de las acciones y precondiciones
def mover(estado, robot, origen, destino, condicion):
    if estado["en"][robot] == origen and estado["condicion"] == condicion:
        return [('en', robot, destino)]
    return []

# Inicialización de las acciones y precondiciones
declare_actions('mover', mover)

# Definición del estado inicial
initial_state = State('estado_inicial')
initial_state["en"] = {"robot1": "sala1"}
initial_state["condicion"] = "normal"

# Definición del estado objetivo
goal_state = State('estado_objetivo')
goal_state["en"] = {"robot1": "sala2"}

# Resolución del problema de planificación
plan = pyhop(initial_state, [('mover', 'robot1', 'sala1', 'sala2', 'normal')], verbose=3)
print(plan)
