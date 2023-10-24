"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: El siguiente código verifica que una palabra o frase ingresada sea un palindromo,
    su modo de función es generar dos listas, una con la palabra o frase y otra invirtiendo la
    palabra o frase, después compara el valor correspondiente a cada posición de ambas listas,
    verificando que sean iguales, si se logra recorrer toda la lista, es un palindromo, en caso
    contrario no es un palindromo
"""

# Pedimos que ingrese una palabra y eliminamos mayúsculas
palabra = str(input("Ingresa tu palabra: ")).lower()

# Remplaza las letras con acento a sus semejantes sin acentos, así como el espacio en blanco
palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "")


# Definimos una función que recibe la palabra
def palindromo(palabra):

    # Inicializa dos listas vacías para almacenar la palabra y la palabra invertida
    lista = []
    lista2 = []

    # Iteramos en el rango del tamaño de la palabra
    for i in range(len(palabra)):
         # Agrega el valor correspondiente a ese indice, en caso de que no sea un espacio vacio
        lista.append(palabra[i])
        lista2.append(palabra[::-1][i])

    es_palindromo = True  # Inicialmente asumimos que es un palíndromo

    # Se imprime las listas
    print(f"Lista 1: {lista}")
    print(f"Lista 2: {lista2}")

    # Iteramos en el rango del tamaño de la palabra
    for i in range(len(palabra)):
        # Verificamos que el valor de la lista sea diferente que el de la lista 2
        if lista[i] != lista2[i]:
            # En caso de ser así, asumimos que no es un palíndromo
            es_palindromo = False
            # Terminamos de iterar
            break
        # En caso de no ser diferente
        else:
            # Mostramos la comparación de los valores de ambas listas
            print(f"Comparando el valor {lista[i]} con {lista2[i]}")

    # En caso de que siga siendo un palindromo
    if es_palindromo:
        # Imprime que es un palindromo
        print("Es un palíndromo")
    # En caso de no ser así
    else:
        # Imprime que noes un palindromo
        print("No es un palíndromo")

# Llama a la función
palindromo(palabra)
