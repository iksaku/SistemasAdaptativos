'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Automatas celulares
 Programa para visualizar una regla del AC 1D
'''

import sys
from automata_celular import *

iteraciones=int(sys.argv[1])
correr(iteraciones, obtener_regla(2))