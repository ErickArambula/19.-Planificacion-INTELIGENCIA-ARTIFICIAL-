from pygraphplan import pgp

# Definir el problema de planificación
problema = pgp.GraphPlanProblem()

# Definir los operadores disponibles
def cargar_paquete(paquete, camion, destino):
    return f"cargar({paquete}, {camion}, {destino})"

def descargar_paquete(paquete, camion, destino):
    return f"descargar({paquete}, {camion}, {destino})"

# Definir los estados iniciales
problema.set_initial_state([
    "en(camion1, almacen)",
    "en(paqueteA, almacen)",
    "en(paqueteB, almacen)",
    "en(camion2, almacen)",
])

# Definir los estados objetivo
problema.set_goal(["en(camion1, destino1)", "en(paqueteA, destino1)"])

# Agregar los operadores al problema
problema.add_operator(cargar_paquete("paqueteA", "camion1", "destino1"))
problema.add_operator(descargar_paquete("paqueteA", "camion1", "destino1"))

# Resolver el problema de planificación con GRAPHPLAN
plan = problema.graphplan()

# Imprimir el plan encontrado
for accion in plan:
    print(accion)
