import random
from bokeh.plotting import figure, show


def tirar_dado(num_tiros):
    secuencia_tiros = []
    for _ in range(num_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_tiros.append(tiro)
    return secuencia_tiros

def simulacion(num_tiros, num_intentos):
    tiros = []
    for _ in range(num_intentos):
        secuencia_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_tiros)
    
    tiros_con_1 = 0
    for tiro in tiros:
        if 6 in tiro:
            tiros_con_1 += 1
    probabilidad_tiros_1 = tiros_con_1 / num_intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {num_tiros} tiros: {probabilidad_tiros_1}')


def simulacion_2(num_tiros, num_intentos):
    tiros = []
    for _ in range(num_intentos):
        secuencia_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_tiros)
    
    tiros_con_6 = 0
    for tiro in tiros:
        if 6 in tiro:
            tiros_con_6 += 1
    probabilidad_tiros_6_dado_1 = tiros_con_6 / num_intentos

    tiros = []
    for _ in range(num_intentos):
        secuencia_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_tiros)
    
    tiros_con_6 = 0
    for tiro in tiros:
        if 6 in tiro:
            tiros_con_6 += 1
    probabilidad_tiros_6_dado_2 = tiros_con_6 / num_intentos

    probabilidad_final = probabilidad_tiros_6_dado_1 * probabilidad_tiros_6_dado_2
    print(f'Probabilidad de obtener por lo menos un 12 en {num_tiros} tiros: {probabilidad_final}')


def main():
    num_tiros = int(input('Ingrese la cantidad de tiros que se realizaran: '))
    num_intentos = int(input('Cuantas veces correra la simulacion?: '))
    num_dados = int(input('Ingrese 1 para usar un dado o 2 para usar dos dados: '))
    if num_dados == 1:
        simulacion(num_tiros, num_intentos)
    
    elif num_dados == 2:
        simulacion_2(num_tiros, num_intentos,)


if __name__ == '__main__':
    main()