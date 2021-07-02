import numpy as np
import pandas as pd
import random
from colocar_no_aleatorio import colocar_no_aleatorio
def inicializamos_tablero_aliado():
    barcos=[1,1,1,1,2,2,2,3,3,4]
    tablero=np.full((10,10),0)
    for i in barcos:
        tablero=colocar_no_aleatorio(i,tablero)
        print(np.where(tablero==1,'O','-'))
    return tablero