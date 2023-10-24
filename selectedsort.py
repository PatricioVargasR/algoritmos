import random

datos = [random.randint(1,50) for _ in range(120)]

def selected(datos):

    for i in range(len(datos)):
        pequeño = i
        print(pequeño)

        for j in range(i+1, len(datos)):
            if datos[j] < datos[pequeño]:
                pequeño = j

        datos[i], datos[pequeño] = datos[pequeño], datos[i]

print(datos)
selected(datos)
print(datos)