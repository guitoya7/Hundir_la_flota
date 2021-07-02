import numpy as np
import pandas as pd
import random
from colocar_aleatorio import colocar_aleatorio

def inicializamos_tablero_enemigo():
    barcos=[1,1,1,1,2,2,2,3,3,4]
    tablero=np.full((10,10),0)
    for i in barcos:
        tablero=colocar_aleatorio(i,tablero)
    return tablero