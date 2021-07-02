import numpy as np
import pandas as pd
import random


def comienza_el_juego(tablero_aliado, tablero_enemigo):
    vida_aliado = 20
    vida_enemigo = 20
    tablero_aliado_disparo = np.full((10, 10), '.')
    tablero_enemigo_disparo = tablero_aliado.astype(object)
    while vida_aliado > 0 and vida_enemigo > 0:
        parada = 0
        while parada == 0:
            disparo_aliadox = int(input('Aliado, dame la coordenada x de tu disparo'))
            disparo_aliadoy = int(input('Aliado, dame la coordenada y de tu disparo'))
            if disparo_aliadox < 0 or disparo_aliadox > 10 or disparo_aliadoy < 0 or disparo_aliadoy > 10:
                print("posicion no valida")
                continue
            if tablero_enemigo[disparo_aliadox, disparo_aliadoy] == 1:
                print('BOOM, le has dado soldado')
                tablero_aliado_disparo[disparo_aliadox, disparo_aliadoy] = 'X'
                print(tablero_aliado_disparo)
                vida_enemigo = vida_enemigo - 1
            else:
                print('BOOM, al agua soldado')
                tablero_aliado_disparo[disparo_aliadox, disparo_aliadoy] = 'F'
                print(tablero_aliado_disparo)
                parada = 1
        parada = 0
        # vamos a agregar un tiempo de espera
        while parada == 0:
            disparo_enemigo = np.random.choice(10, 2, replace=True)

            if tablero_aliado[disparo_enemigo[0], disparo_enemigo[1]] == 1:
                print('BOOM, nos han dado')
                tablero_enemigo_disparo[disparo_enemigo[0], disparo_enemigo[1]] = 'X'
                print(np.where((np.where(tablero_enemigo_disparo == 1, "O", tablero_enemigo_disparo)) == 0, '-',
                               (np.where(tablero_enemigo_disparo == 1, "O", tablero_enemigo_disparo))))
                vida_aliado = vida_aliado - 1
            else:
                print('BOOM, por los pelos casi nos han dado')
                tablero_enemigo_disparo[disparo_enemigo[0], disparo_enemigo[1]] = 'F'
                print(np.where((np.where(tablero_enemigo_disparo == 1, "O", tablero_enemigo_disparo)) == 0, '-',
                               (np.where(tablero_enemigo_disparo == 1, "O", tablero_enemigo_disparo))))
                parada = 1

    if vida_aliado > 0:
        print('Gana aliado')
    else:
        print('Gana enemigo')
