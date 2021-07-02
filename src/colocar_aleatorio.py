import numpy as np
import pandas as pd
import random

def colocar_aleatorio(tamaño_barco,tablero):
    direccion=np.array(['N','S','E','O'])
    while True:
        direccion=random.choice(direccion)
        posicion=np.random.choice(10,2,replace=True)
        if direccion=='E':
            if posicion[1]-tamaño_barco<0:
                continue
            else:
                if np.sum(tablero[posicion[0],posicion[1]:posicion[1]-tamaño_barco:-1])==0:
                    tablero[posicion[0],posicion[1]:posicion[1]-tamaño_barco:-1]=1
                    break
                else:
                    a=0
        elif direccion=='O':
            if posicion[1]+tamaño_barco>9:
                continue
            else:
                if np.sum(tablero[posicion[0],posicion[1]:posicion[1]+tamaño_barco])==0:
                    tablero[posicion[0],posicion[1]:posicion[1]+tamaño_barco]=1
                    break
                else:
                    a=0
        elif direccion=='N':
            if posicion[0]-tamaño_barco<0:
                continue
            else:
                if np.sum(tablero[posicion[0]:posicion[0]-tamaño_barco:-1,posicion[1]])==0:
                    tablero[posicion[0]:posicion[0]-tamaño_barco:-1,posicion[1]]=1
                    break
                else:
                    a=0
        elif direccion=='S':
            if posicion[0]+tamaño_barco>9:
                continue
            else:
                if np.sum(tablero[posicion[0]:posicion[0]+tamaño_barco,posicion[1]])==0:
                    tablero[posicion[0]:posicion[0]+tamaño_barco,posicion[1]]=1
                    break
                else:
                    a=0
    return tablero