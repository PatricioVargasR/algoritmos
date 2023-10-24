"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: El siguiente código es la representación del problema de las 8 reinas.
    El problema consiste en un tablero de 8 x 8, en donde tendremos 8 reinas que posicionar,
    estas piezas no se deben de interceptar en sus filas, columnas y diagonales colindantes.
    El código deja que el usuario complete el juego
"""

# Creamos una función que almacena el tablero
def crear_tablero():
    tablero = [
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
        [" ", " ", " ", " "," ", " ", " ", " "],
    ]
    # Regresa el tablero
    return tablero

# Función que imprime el tablero, necesita el tablero como parámetor
def imprimir_tablero(tablero):
    # Itera por cada elemento del tabero
    for i in tablero:
        # Imprime el elemento
        print(i)

# Funciones que verfician bloquean las diagonales colindantes

# Función para verificar la diagona derecha de arriba
def diagonal_arriba(fila, columna, tablero):
    # Inicializa dos dos contadores
    i = 0
    j = 0
    # Mientras la filas y columnas + 1 restandole el valor del contador, sean mayores que cero
    while fila + 1 - i > 0 and columna + 1 - j > 0:
        # A las posiciones correspondientes, se les asigna el valor del asterisco
        tablero[fila - i][columna - j] = "*"
        # Aumenta el uno a los contadores
        i += 1
        j += 1
    # Regresa el tablero
    return tablero

# Función para verificar la diagona derecha de abajo
def diagonal_abajo(fila, columna, tablero):
    # Inicializa dos dos contadores
    i = 0
    j = 0
    # Mientras la fila sumando el valor de contador  y columnas mas el contador, sean menores a 8
    while fila + i < 8 and columna + j < 8:
        # A las posiciones correspondientes, se les asigna el valor de 
        tablero[fila + i][columna +j] = "*"
        # Aumenta el uno a los contadores    
        i += 1
        j += 1
    return tablero

# Función para verificar la diagona izquierda de abajo
def diagonal_abajo2(fila, columna, tablero): 
    # Inicializa dos dos contadores
    i = 0
    j = 0
    # Mientras la fila restando el valor de contador y sumando 1  y columnas mas el contador, sean menores a 8
    while fila + 1 - i > 0 and columna + j < 8:
        # A las posiciones correspondientes, se les asigna el valor de 
        tablero[fila - i][columna + j] = "*"
        # Aumenta el uno a los contadores
        i += 1
        j += 1
    return tablero

# Función para verificar la diagonl izquierda de arriba
def diagonal_arriba2(fila, columna, tablero): 
    # Inicializa dos dos contadores
    i = 0
    j = 0
    # Mientras la fila sumando el valor de contador y columnas + 1 restandole el valor del contador, sean mayores que cero
    while fila + i < 8 and columna + 1 - j > 0:
        # A las posiciones correspondientes, se les asigna el valor de 
        tablero[fila + i][columna - j] = "*"
        # Aumenta el uno a los contadores
        i += 1
        j += 1

    # Una vez se terminan de colocar todas las areas bloqueadas, se asigna el icono de la reina
    tablero[fila][columna] = "R"
    # Regresa el tablero
    return tablero

# Función que bloquea las filas y columnas correspondientes
def definir_espacios(tablero, fila, columna):
    # Asignamos el icono que representa a la reina en las coordenadas del usuario
    # tablero[fila][columna] = "R"
    # Itera i en un rango de 8 veces
    for i in range(8):
        # Si la fila con la columna cambiante es diferente al asterico *
        if tablero[fila][i] != "*":
            # Asignna el valor correspondiente a la coordenada
            tablero[fila][i] = "*"
        # Si la columna con la fila cambiante es diferente al asterico *
        if tablero[i][columna] != "*":
            # Asignna el valor correspondiente a la coordenada
            tablero[i][columna] = "*"

# Definimos una función para iniciar todo
def jugar():
    # Asigna el valor de la función crear_tablero a la variable tablero
    tablero = crear_tablero()
    # Crea una variable que almacena el total de reinas
    reinas = 8
    # Mientras sea verdad el siugiente bloque
    while True:

        # Imprime las reinas restantes
        print(f"Reinas restantes: {reinas}")

        # Imprime el tablero
        imprimir_tablero(tablero)

        # El usuario ingresa las coordenadas
        fila = int(input("Elige una fila (0 a 7): "))
        columna = int(input("Elige una columna (0 a 7): "))

        # Si las coordenadas son mayores a las opciones posibles
        if fila > 7 and columna > 7:
            # Manda un mensaje de advertencia
            print("Opción invalida")
            # Sigue con el código
            continue
        
        # Si en la coordenada ingresada, el valor es diferente al asterisoc y es igual a un espacio vacío
        if tablero[fila][columna] != "*" and tablero[fila][columna] == " ":
            # Llama a las funciones para definir espacios, con las coordeandas y tablero de parametro
            definir_espacios(tablero, fila, columna)  
            diagonal_abajo(fila, columna, tablero)
            diagonal_arriba(fila, columna, tablero)
            diagonal_abajo2(fila, columna, tablero)
            diagonal_arriba2(fila, columna, tablero)
            # Se resta uno a la reinas disponibles
            reinas -= 1
        # En caso de no estar desocupada
        else:
            # Manda una advertencia
            print("Esa casilla no es accesible")
            # Continua sin ningún cambio
            continue
        
        # Si las reinas se han colocado totalmente
        if reinas == 0:
            # Manda mensaje de felicitación
            print("Terminaste el juego!")
            # Imprime el ultimo tablero
            imprimir_tablero(tablero)
            # Termina el bucle
            break

# Llama a la función jugar
jugar()

        