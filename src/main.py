import numpy as np
import pandas as pd
import random

from inicializamos_tablero_aliado import inicializamos_tablero_aliado
from inicializamos_tablero_enemigo import inicializamos_tablero_enemigo
from comienza_el_juego import comienza_el_juego

tablero_enemigo = inicializamos_tablero_enemigo()
print(np.where(tablero_enemigo==1,'O','-'))
tablero_aliado = inicializamos_tablero_aliado()
comienza_el_juego(tablero_aliado,tablero_enemigo)