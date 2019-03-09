def funcion_nucleo(entrada):
    n_valores = len(entrada)
    return sum(
        [pesos[n] * entrada[n] for n in range(n_valores)]
    )


def funcion_activacion(resultado_nucleo):
    return resultado_nucleo >= 0


max_iter = 50

tasa_aprendizaje = 0.1

pesos = [1, 0, 0, 0, 0, 0, 0]

entradas = [
    # [Valores de Entrada], <Resultado esperado>
    # El primer valor en [Valores de Entrada] es el Sesgo (-1) y es el mismo para todas las entradas
    [[-1, 1, 0, 1, 0, 0, 0], 1],
    [[-1, 1, 0, 1, 1, 0, 0], 1],
    [[-1, 1, 0, 1, 0, 1, 0], 1],
    [[-1, 1, 1, 0, 0, 1, 1], 1],
    [[-1, 1, 1, 1, 1, 0, 0], 1],
    [[-1, 1, 0, 0, 0, 1, 1], 1],
    [[-1, 1, 0, 0, 0, 1, 0], 0],
    [[-1, 0, 1, 1, 1, 0, 1], 1],
    [[-1, 0, 1, 1, 0, 1, 1], 0],
    [[-1, 0, 0, 0, 1, 1, 0], 0],
    [[-1, 0, 1, 0, 1, 0, 1], 0],
    [[-1, 0, 0, 0, 1, 0, 1], 0],
    [[-1, 0, 1, 1, 0, 1, 1], 0],
    [[-1, 0, 1, 1, 1, 0, 0], 0]
]

iteraciones = 0
pincorrectos = 1.0

while pincorrectos > 0.2 and iteraciones < max_iter:

    incorrectos = 0

    print('\nITERACION ' + str(iteraciones) + '\n')

    for c_entrada in entradas:
        print('Procesando entrada: ')
        print(str(c_entrada[0]) + '\n')

        y = funcion_activacion(funcion_nucleo(c_entrada[0]))
        d = c_entrada[1]
        if y != d:
            incorrectos = incorrectos + 1
            print('ACTUALIZANDO PESOS')
            for i in range(len(pesos)):
                pesos[i] += tasa_aprendizaje * pesos[i] * (d - y)
                print('\tw' + str(i) + ': ' + str(pesos[i]))
            print()

    pincorrectos = incorrectos * 1.0 / len(entradas)
    print(str(pincorrectos * 100) + '% de entradas procesadas incorrectamente')
    iteraciones += 1

print('\nPesos finales:')

for i in range(len(pesos)):
    print('\tw' + str(i) + ': ' + str(pesos[i]))
