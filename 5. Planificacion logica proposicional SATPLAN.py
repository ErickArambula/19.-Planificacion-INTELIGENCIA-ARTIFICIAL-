from pddlpy import DomainProblem
from satplan import SATPlan

# Definir el dominio y el problema en lenguaje PDDL
domain = """
(define (domain transporte)
  (:requirements :strips)
  (:predicates (en_camion ?paquete ?camion)
              (en_almacen ?paquete)
              (en_destino ?paquete ?destino)
              (camion_vacio ?camion)
              (en_destino_correcto ?paquete)
              (mismo_destino ?paquete1 ?paquete2)
              (diferente_paquete ?paquete1 ?paquete2)
              (cargar ?paquete ?camion ?destino)
              (descargar ?paquete ?camion ?destino)
  )
  (:action cargar
    :parameters (?paquete - paquete ?camion - camion ?destino - destino)
    :precondition (and (en_almacen ?paquete) (en_camion ?paquete ?camion) (en_destino_correcto ?paquete) (camion_vacio ?camion))
    :effect (and (not (en_almacen ?paquete)) (en_camion ?paquete ?camion) (en_destino ?paquete ?destino) (not (camion_vacio ?camion)))
  )
  (:action descargar
    :parameters (?paquete - paquete ?camion - camion ?destino - destino)
    :precondition (and (en_camion ?paquete ?camion) (en_destino ?paquete ?destino))
    :effect (and (en_almacen ?paquete) (not (en_camion ?paquete ?camion)) (not (en_destino ?paquete ?destino)) (camion_vacio ?camion))
  )
)
"""

problem = """
(define (problem transporte-1)
  (:domain transporte)
  (:objects paqueteA - paquete paqueteB - paquete camion1 - camion almacen - almacen destino1 - destino destino2 - destino)
  (:init (en_camion paqueteA camion1) (en_almacen paqueteA) (en_almacen paqueteB) (camion_vacio camion1) (en_almacen paqueteB) (en_almacen paqueteB) (en_destino_correcto paqueteA) (en_destino_correcto paqueteB) (mismo_destino destino1 destino1) (mismo_destino destino2 destino2) (diferente_paquete paqueteA paqueteB) (diferente_paquete paqueteB paqueteA))
  (:goal (and (en_destino paqueteA destino1)))
)
"""

# Crear un objeto DomainProblem con el dominio y el problema
dp = DomainProblem(domain, problem)

# Resolver el problema utilizando SATPLAN
solucion = SATPlan(dp, verbose=2)

# Imprimir el plan encontrado
for accion in solucion:
    print(accion)
