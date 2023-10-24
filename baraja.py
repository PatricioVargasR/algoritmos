"""
    Alumno: Patricio de Jesús Vargas Ramírez
    Grupo: TI-41
    Descripción: El siguiente código es una representación de "barajear" la baraja española de 40 cartas
    se cuenta con dos mazos de 20 cartas cada uno, en primera parte, se une ambos mazos desde arriba,
    luego se vuelven a separar en partes igual, para ser unidas nuevamente, pero en este caso, siendo tomadas
    desde la parte de abajo.
"""

# Listas que contienen las cartas de la baraja española
# a: contiene oros y copas
# b: contiene espadas y bastos
a = ["1O", "2O", "3O", "4O", "5O", "6O", "7O", "SO", "CO", "RO", "1C", "2C", "3C", "4C", "5C", "6C", "7C", "SC", "CC", "RC"]
b = ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "SE", "CE", "RE", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "SB", "CB", "RB"]

# Definimos una función que recibirá a ambas listas como parámetros
def barajear(a, b):

    # Lista vacía que utilizaremos para juntar los mazos
    barajeado = []

    # Iteramos en a
    for i in a:
        # iteramos en b
        for j in b:
            # Si los elementos de a y b no están en la lista barajeado, los agrega
            if i not in barajeado and j not in barajeado:
                barajeado.append(i)
                barajeado.append(j)

    # Imprime la primera lista donde se juntaron
    print(f"Primera barajeada: {barajeado} \n")

    # Obtiene la mitad de la lista
    mitad = int(len(barajeado)/2)

    # En una nueva lista, toma los valores de la primera mitad de la lista mezclada
    primera_mitad = barajeado[:mitad]
    print(f"Primera mitad mezclada: {primera_mitad} \n")
    # En una nueva lista, toma los valores de la segunda mitad de la lista mezclada
    segunda_mitad = barajeado[mitad:]
    print(f"Segunda mitad mezclada: {segunda_mitad} \n")

    # Inicializa una lista para la barajeada final
    final = []

    # Itera por cada elemento de la primera mitad, invirtiendo la lista
    for i in primera_mitad[::-1]:
        # Itera por cada elemento de la primera mitad, invirtiendo la lista
        for j in segunda_mitad[::-1]:
            # Si los elementos de i y j no están en la lista barajeado, los agrega
            if i not in final and j not in final:
                final.append(i)
                final.append(j)

    # Regresa la lista final
    return final

# Imprime un mensaje
print("Datos de entrada: \n")
# Muestra la primera lista de 20 cartas
print(f"Primer mazo de 20: {a} \n")
# Muestra la segunda lista de 20 cartas
print(f"Segundo mazo de 20: {b} \n")
# Imprime la lista ya barajeada
print(f"Mazo totalmente mezclado: {barajear(a, b)}")
