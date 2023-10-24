"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: Este código utiliza la librería random para crear una lista de 120 datos aleatorios,
    que luego se ordenan utilizando el algoritmo quicksort. Quicksort divide la lista y la ordena
    recursivamente.
"""

# Importamos la librería random
import random

# Generamos una lista de 120 números aleatorios comprendidos entre 1 y 50
# datos = [random.randint(1, 50) for _ in range(120)]

datos = ["a", "c", "d", "b"]
# Definimos una función que recibe como parámetro la lista
def quicksort(datos):
    
    # Verificamos si el tamaño de la lista es mayor a 1
    if len(datos) > 1: 
        # Calculamos el índice del valor medio, dividiendo el tamaño de la lista entre 2
        piv = int(len(datos) / 2)
        # Obtenemos el valor del medio
        valor = datos[piv]

        # Dividimos los valores en tres partes: izquierda, medio y derecha
        izquierda = [i for i in datos if i < valor]
        medio = [i for i in datos if i == valor]
        derecha = [i for i in datos if i > valor]

        # Llamamos a la función quicksort de forma recursiva para las listas izquierda y derecha,
        # y luego concatenamos el resultado con la lista de valores medios
        resto = quicksort(izquierda) + medio + quicksort(derecha)
        
        # Devolvemos la lista ordenada
        return resto
    # Si el tamaño de la lista es 1 o menos, simplemente devolvemos la lista
    else:
        return datos

# Imprimimos la lista original
print(datos)

# Imprimimos la lista ordenada utilizando quicksort
print(quicksort(datos))
