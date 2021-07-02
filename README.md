# Hundir_la_flota
Apasionante juego donde deberás salvar a tu tripulación de las manos del almirante Nikolái Guerásimovich Kuznetsov.

## Reglas del juego:

1. Hay dos jugadores: tu y la maquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos de Nikolái se colocan de manera aleatoria. Los tuyos tendrás que colocarlos asignando una coordenada de inicio y una dirección entre N S E O. La flota de ambos será:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora
4. Tanto tu, como la Nikolái tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tu.
6. En cada turno disparas a una coordenada (Y, X) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca al almirante.
7. En los turnos de la maquina, si acierta, también le vuelve a tocar.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.

## Descripción del proyecto:
Realizamos cinco funciones: (comienza_el_juego
1. colocar_aleatorio: En un tablero 10*10 colocamos de manera aleatoria un barco con un algoritmo de control para que no lo coloque en una posicion ya usada ni se salga del tablero.
2. inicializamos_tablero_enemigo: Llama la funcion anterior para cada barco del juego.
3. colocar_no_aleatorio: Pide al usuario coordenada para inicializar barco y dirección, con el mismo algoritmo de control de antes.
4. inicializamos_tablero_aliado: Llama la funcion anterior para cada barco del juego.
5. comienza_el_juego: Programa que guarda la vida de cada jugador (numero de barcos) y inicializa cada disparo devolviendo un mapa con tus disparos y otro con los del rival.

Algoritmo de control: Cada posición del barco es un 1 numérico, si queremos colocar un barco nuevo sumamos las posiciones adyacentes y si su suma es cero, no habrá barco.

## Librerias:
1. Numpys 
2. Pandas
3. Random

## Recursos:
1. Pycharm






Autores: 
1. Pablo Faura Sanz  
2. Yago García Marqués
