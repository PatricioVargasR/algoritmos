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
    return tablero

def imprimir_tablero(tablero):
    for i in tablero:
        print(i)

def diagonal_arriba(fila, columna, tablero):
    i = 0
    j = 0
    while fila + 1 - i > 0 and columna + 1 - j > 0:
        tablero[fila - i][columna - j] = "*"
        i += 1
        j += 1
    return tablero

def diagonal_abajo(fila, columna, tablero):
    i = 0
    j = 0
    while fila + i < 8 and columna + j < 8:
        tablero[fila + i][columna +j] = "*"
        i += 1
        j += 1
    return tablero

def diagonal_abajo2(fila, columna, tablero): 
    i = 0
    j = 0
    while fila + 1 - i > 0 and columna + j < 8:
        tablero[fila - i][columna + j] = "*"
        i += 1
        j += 1
    return tablero

def diagonal_arriba2(fila, columna, tablero): 
    i = 0
    j = 0
    while fila + i < 8 and columna + 1 - j > 0:
        tablero[fila + i][columna - j] = "*"
        i += 1
        j += 1

    tablero[fila][columna] = "R"
    return tablero

def definir_espacios(tablero, fila, columna):
    for i in range(8):
        if tablero[fila][i] != "*":
            tablero[fila][i] = "*"
        if tablero[i][columna] != "*":
            tablero[i][columna] = "*"

def jugar():
    tablero = crear_tablero()
    reinas = 8
    while True:
        print(f"Reinas restantes: {reinas}")
        imprimir_tablero(tablero)
        fila = int(input("Elige una fila (0 a 7): "))
        columna = int(input("Elige una columna (0 a 7): "))
        if fila > 7 and columna > 7:
            print("Opción invalida")
            continue
        if tablero[fila][columna] != "*" and tablero[fila][columna] == " ":
            definir_espacios(tablero, fila, columna)  
            diagonal_abajo(fila, columna, tablero)
            diagonal_arriba(fila, columna, tablero)
            diagonal_abajo2(fila, columna, tablero)
            diagonal_arriba2(fila, columna, tablero)
            reinas -= 1
        else:
            print("Esa casilla no es accesible")
            continue
        if reinas == 0:
            print("Terminaste el juego!")
            imprimir_tablero(tablero)
            break

jugar()
