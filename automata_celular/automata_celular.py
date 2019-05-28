"""
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software

 Programacion de Sistemas Adaptativos
 Automatas celulares
 Automata con celdas binarias, donde cada celda tiene dos vecinos (1D)

 Modificado por Jorge González. Matricula: 1889169
 Se puede utilizar este código con cualquier regla... Instrucciones en la línea 38 de este archivo.
"""

import sys

def imprime_resultado(cadena):
    resultado_formato = '_'
    for caracter in cadena:
        if caracter == '1':
            resultado_formato = resultado_formato + '*'
        else:
            resultado_formato = resultado_formato + ' '
    print(resultado_formato + "_")


# Regla 165: Vecinos con el mismo color=1, de otra manera=0
# def procesa_ventana(ventana):
#     if ventana[0] == ventana[2]:
#         resultado = '1'
#     else:
#         resultado = '0'
#     return resultado

# Regla Automática
def procesa_ventana(ventana, regla=None):
    if regla == None:
        regla = 69
    ventana_bin = int(''.join(ventana), 2)
    regla = '{0:08b}'.format(regla)[::-1]
    return regla[int(ventana_bin)]


def recorre_cadena(cadena, regla=None):
    nueva_cadena = ''

    for i in range(0, len(cadena)):
        n = len(cadena)
        ventana = cadena[(i + (n - 1)) % n] + cadena[i] + cadena[(i + 1) % n]
        nueva_cadena = nueva_cadena + procesa_ventana(ventana, regla)

    return nueva_cadena


def correr(iteraciones, regla=None):
    cadena1 = "0000000000000000000000000000000000100000000000000000000000000000000000"
    # cadena2="0000100000"

    # cadena_actual = "00000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000"
    cadena_actual = cadena1

    for i in range(0, int(iteraciones)):
        imprime_resultado(cadena_actual)
        nueva_cadena = recorre_cadena(cadena_actual, regla)
        cadena_actual = nueva_cadena


def obtener_regla(input_index):
    try:
        return int(sys.argv[input_index])
    except IndexError:
        return None
