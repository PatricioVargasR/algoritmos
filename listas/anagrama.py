"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: El siguiente código verifica que dos palabras o frases ingresadas sean un anagrama,
    genera dos listas, correspondiente a cada palabra, veificando primero que tenga la misma longitud,
    en caso de que sea verdad, verifica que las letras de la palabra 1 existan en la palabra dos,
    eliminando las coincidencias, hasta que la palabra 2 sea eliminada completamente.
"""


# Pedimos que ingrese las palabras a comparar
palabra = str(input("Ingresa tu palabra: ")).lower()
palabra2 = str(input("Ingrese su segunda palabra: ")).lower()

# Remplaza las letras con acento a sus semejantes sin acentos, así como el espacio en blanco
palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "")
palabra2 = palabra2.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "")

# Creamos una función que reciba ambas palabras como parámetros
def anagrama(palabra, palabra2):

    # Inicializamos dos listas
    lista1 = []
    lista2 = []

    # Verifica que tengan diferente tamaño
    if len(palabra) != len(palabra2):
        # Regresa que no es un anagrama, en caso de ser así
        return "No es un anagrama"

    # Itera en el rango del tamaño de la palabra
    for i in range(len(palabra)):
        # Agrega el valor correspondiente a ese indice
        lista1.append(palabra[i])
        lista2.append(palabra2[i])

    # Se imprime las listas
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    es_anagrama = True # Inicialmente asumimos que es un anagrama

    # Iteramos en el rango del tamaño de la lista2
    for i in range(len(lista2)):
        # En caso de que la letra de la lista1 no exista en lista2
        if lista1[i] not in lista2:
            # Asumimos que no es un anagrama
            es_anagrama = False
            # Terminamos la iteración
            break
        # En caso de no ser verdad
        else:
            # Imrprime la letra que se busca en la lista2
            print(f"Buscando el valor {lista1[i]} en la lista {lista2}")
            print(f"Se encontró el valor {lista1[i]}") # Muestra que letra se encontró en la lista
            lista2.remove(lista1[i]) # Elima la letra encontrada de la lista2

    # En caso de que siga siendo un anagrama
    if es_anagrama:
        # Imprime que es un anagrama
        print("Es un anagrama")
    # En caso de no ser verdad
    else:
        # Imprime que no es un anamagra
        print("No es un anagrama")

# Llama la fucnión
anagrama(palabra, palabra2)
