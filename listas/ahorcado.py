import random

def iniciar_tablero(palabra):
    valor = []
    for i in range(len(palabra)):
        valor.append('_')
    return valor

# def elegir_palabra():
#     C1 = {1:"OVALO", 2:"ADIOS", 3:"BIENVENIDA"}
#     C2 = {1:"OVALO", 2:"ADIOS", 3:"BIENVENIDA"}
#     C3 = {1:"OVALO", 2:"ADIOS", 3:"BIENVENIDA"}

#     categoria = random.choice(["C1", "C2", "C3"])
#     posicion = random.randint(1,3)

#     if categoria == "C1":
#         palabra = C1[posicion]
#         return palabra, categoria
#     elif categoria == "C2":
#         palabra = C2[posicion]
#         return palabra, categoria
#     else:
#         palabra = C3[posicion]
#         return palabra, categoria

# Forma más clara

def elegir_palabra():
    palabras_por_categoria = {
    "C1": ["OVALO", "ADIOS", "BIENVENIDA"],
    "C2": ["OVALO", "ADIOS", "BIENVENIDA"],
    "C3": ["OVALO", "ADIOS", "BIENVENIDA"]
}
    categoria = random.choice(["C1", "C2", "C3"])
    palabra = random.choice(palabras_por_categoria[categoria])
    return palabra, categoria

def jugar():
    print("Bienvenido al ahorcado")
    palabra, categoria = elegir_palabra()
    tablero = iniciar_tablero(palabra)

    print(f"Tu categoria es: {categoria}")

    vidas = 6
    aciertos = 0

    while True:
        print(f"Vidas restantes: {vidas}")
        print(tablero)

        letra = str(input("Ingresa tu letra: ")).upper()

        if (len(letra)) > 1:
            print("Solo escribe una letra")
            continue

        if letra in tablero:
            print("La letra ya está seleccionada")
            continue

        if letra in palabra:
            for i in range(len(palabra)):
                if letra in palabra[i]:
                    indice = i
                    tablero[indice] = letra
                    aciertos += 1
        else:
            vidas -= 1
            print("Letra incorrecta")

        if vidas == 0:
            print(tablero)
            print("Has perdido")
            break

        if aciertos == len(tablero):
            print(tablero)
            print("Has ganado!!!")
            break

jugar()