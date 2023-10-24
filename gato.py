"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: Este código permite jugar al "gato" o tres en raya utilizando una matriz.
    La elección del primer jugador se realiza de manera aleatoria utilizando la librería random.
"""

import random  # Importamos la librería random

# Definimos una función para crear el tablero
def iniciar_tablero():
    # Creamos el tablero utilizando matrices
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # Devolvemos el tablero
    return tablero

# Definimos una función para imprimir el tablero en pantalla
def imprimir_tablero(tablero):
    # Por cada fila en el tablero
    for fila in tablero:
        # Imprimimos esa fila
        print(fila)

# Definimos una función para elegir el ganador
def definir_ganador(tablero, jugador):
    # Iteramos en una posición del tablero
    for i in range(3):
        # Verificamos las filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            # Regresamos verdadero en caso de que alguna fila esté completa
            return True
        # Verificamos las columnas
        elif tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            #  Regresamos verdadero en caso de que alguna columna esté completa
            return True
    # Verificamos las diagonales de izquierda a derecha
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        # Regresamos verdadero en caso de que alguna diagonal esté completa
        return True
    # Verificamos las diagonales de derecha a izquierda
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        # Regresamos verdadero en caso de que alguna diagonal esté completa
        return True
    # En caso de no ser ninguna, regresamos falso
    return False

# Definimos una función para determinar quién empieza
def determinar_primer_jugador():
    # Le damos la opción X u O
    return random.choice(["X", "O"])

# Definimos una función para jugar
def jugar():
    # Asignamos el valor de la función a la variable tablero
    tablero = iniciar_tablero()
    # Asignamos el valor de la función a la variable jugador_actual
    jugador_actual = determinar_primer_jugador()

    # Inicializamos un contador
    jugadas = 0

    # Mientras sea verdad, ejecutará el siguiente código
    while True:
        # Imprimimos el jugador que le toca en ese turno
        print(f"\nTurno del jugador: {jugador_actual}")
        print()
        # Imprimimos el tablero
        imprimir_tablero(tablero)
        print()

        # Pedimos al usuario que elija una coordenada
        fila = int(input("Elige una fila (0, 1 o 2): "))
        columna = int(input("Elige una columna (0, 1 o 2): "))

        # En caso de que la opción no esté permitida
        if fila > 2 or columna > 2:
            # Manda una opción inválida
            print("Opción inválida")
            # Continúa sin asignar
            continue
        
        # Verificamos que la coordenada no esté ocupada
        if tablero[fila][columna] == " ":
            # El icono de la coordenada será el del jugador actual
            tablero[fila][columna] = jugador_actual
            # Aumenta en uno el contador
            jugadas += 1
        # En caso de que no esté vacía
        else:
            # Imprime un mensaje diciendo que la casilla está ocupada
            print("Esa casilla ya está ocupada. Inténtalo de nuevo")
            # Sigue continuando, sin asignar
            continue
        
        # Verificamos si ya hay un ganador
        if definir_ganador(tablero, jugador_actual):
            # Imprimimos el tablero
            imprimir_tablero(tablero)
            # Mencionamos que el jugador ha ganado
            print(f"¡Jugador {jugador_actual} ha ganado!")
            # Termina el juego
            break
        # Si el contador de jugadas llega a nueve
        elif jugadas == 9:
            # Imprimimos el tablero
            imprimir_tablero(tablero)
            # Mencionamos que es un empate
            print("Empate")
            # Termina el juego
            break
        
        # Cambia jugador

        # Si el jugador actual es X
        if jugador_actual == "X":
            # El siguiente jugador será O
            jugador_actual = "O"
        # En cambio
        else:
            # Será X
            jugador_actual = "X"

# Llama a la función jugar
jugar()
