from pyhop import *

# Declaración de las acciones y precondiciones
def mover(estado, robot, origen, destino):
    if estado["en"][robot] == origen:
        return [('en', robot, destino)]

def coordinar_acciones(estado, robot1, robot2, objetivo):
    if estado["en"][robot1] == objetivo and estado["en"][robot2] == objetivo:
        return [('objetivo_comun', objetivo)]

# Inicialización de las acciones y precondiciones
declare_actions('mover', mover)
declare_actions('coordinar_acciones', coordinar_acciones)

# Definición del estado inicial
initial_state = State('estado_inicial')
initial_state["en"] = {"robot1": "sala1", "robot2": "sala2"}

# Definición del estado objetivo
goal_state = State('estado_objetivo')
goal_state["en"] = {"robot1": "sala2", "robot2": "sala2"}

# Planificación multiagente
plan = pyhop(initial_state, [('mover', 'robot1', 'sala1', 'sala2'),
                            ('mover', 'robot2', 'sala2', 'sala2'),
                            ('coordinar_acciones', 'robot1', 'robot2', 'sala2')],
             verbose=3)
print("Plan multiagente:", plan)
