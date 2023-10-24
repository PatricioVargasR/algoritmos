# cantidad_personas = ["1P", "2P", "3P", "4P"]

cartas = [5, 6, 7, 2]

sobrantes = []

# for i in cantidad_personas:
#     cantidad = int(input(f"Ingresa la catidad de cartas de la persona {i}: "))
#     cartas.append(cantidad)

print(cartas)

for i in range(len(cartas)):
    if cartas[i] >= 5:
        restante = cartas[i]-5
        if restante == 0:
            continue
        cartas[i] = restante
        sobrantes.append(restante)
    else:
        cartas.pop(i)
    


print("Cartas: ", cartas)
print("Sobrante",sobrantes)
    
