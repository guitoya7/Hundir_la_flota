import numpy as np
import pandas as pd
import random

def colocar_no_aleatorio(tamaño_barco,tablero):
    print('Vamos a colocar un barco de dimensión:',tamaño_barco)
    direccion=np.array(['N','S','E','O'])
    while True:
        posicionx=int(input('Inicializa coordenada x'))
        posiciony=int(input('Inicializa coordenada y'))
        posicion=[posicionx,posiciony]
        direccion=input('Escoge dirección en la que avanza tu barco')
        if posicionx < 0 or posicionx > 10 or posiciony < 0 or posiciony > 10:
            print("posicion no valida")
            continue
        if direccion=='E':
            if posicion[1]-tamaño_barco<0:
                continue
            else:
                if np.sum(tablero[posicion[0],posicion[1]:posicion[1]-tamaño_barco:-1])==0:
                    tablero[posicion[0],posicion[1]:posicion[1]-tamaño_barco:-1]=1
                    break
                else:
                    print('Estas pisando otro barco, vuelve a intentarlo')
        elif direccion=='O':
            if posicion[1]+tamaño_barco>9:
                continue
            else:
                if np.sum(tablero[posicion[0],posicion[1]:posicion[1]+tamaño_barco])==0:
                    tablero[posicion[0],posicion[1]:posicion[1]+tamaño_barco]=1
                    break
                else:
                    print('Estas pisando otro barco, vuelve a intentarlo')
        elif direccion=='N':
            if posicion[0]-tamaño_barco<0:
                continue
            else:
                if np.sum(tablero[posicion[0]:posicion[0]-tamaño_barco:-1,posicion[1]])==0:
                    tablero[posicion[0]:posicion[0]-tamaño_barco:-1,posicion[1]]=1
                    break
                else:
                    print('Estas pisando otro barco, vuelve a intentarlo')
        elif direccion=='S':
            if posicion[0]+tamaño_barco>9:
                continue
            else:
                if np.sum(tablero[posicion[0]:posicion[0]+tamaño_barco,posicion[1]])==0:
                    tablero[posicion[0]:posicion[0]+tamaño_barco,posicion[1]]=1
                    break
                else:
                    print('Estas pisando otro barco, vuelve a intentarlo')
    return tablero