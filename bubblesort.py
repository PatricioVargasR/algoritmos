"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: Utilizando la librería random, creamos una lista de 10 
    valores comprendidos entre los números 1 y 50. Luego, ordenamos la lista
    utilizando el algoritmo de ordenamiento burbuja (bubblesort).
"""

# Importamos la librería random
import random

# Definimos una función que recibe una lista como parámetro
def ordenamiento(datos):
    
    # Obtenemos el tamaño de la lista
    tamaño = len(datos)
    # Iteramos a través del tamaño del array
    for i in range(tamaño):
        # Iteramos en un rango de 0 a tamaño - i - 1
        for j in range(0, tamaño - i - 1):
            # Si el valor en la posición actual es mayor que el siguiente valor
            if datos[j] > datos[j+1]:
                # Intercambiamos los valores para ordenarlos
                datos[j], datos[j+1] = datos[j+1], datos[j]

# Creamos una lista de 10 números aleatorios entre 1 y 50
datos = [random.randint(1, 50) for _ in range(10)]

# Imprimimos la lista original
print(datos)
# Llamamos a la función para ordenar la lista
ordenamiento(datos)
# Imprimimos la lista ordenada
print(datos)
