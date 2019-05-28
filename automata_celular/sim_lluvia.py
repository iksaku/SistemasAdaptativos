'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Automatas celulares
 Programa que simula una lluvia de meteoritos utilizando automatas celulares
'''

import sys
import math
import random
import pygame
from meteor import *
from automata_celular import *


posiciones=[[100,100],[100,500],[200,300],[200,400],[300,100],[300,300],[300,600],[400,300],[400,500],[500,200],[500,600]]
configuracion_actual="00000100000"

if(len(sys.argv)<2):
	for i in range(len(posiciones)):
		crear_meteoro(posiciones[i][0],posiciones[i][1])
else:
	iteraciones=int(sys.argv[1])
	for i in range(iteraciones):
		print(configuracion_actual)
		j=0
		for celda in configuracion_actual:
			if int(celda)==1:
				crear_meteoro(posiciones[j][0],posiciones[j][1])
			j=j+1
		nueva_configuracion=recorre_cadena(configuracion_actual, obtener_regla(1))
		configuracion_actual=nueva_configuracion
	
