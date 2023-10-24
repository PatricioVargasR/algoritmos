from clasePila import Pila

def calculadora_polaca(elementos):
    p = Pila()
    for elemento in elementos:
        print("DEBUG:", elemento)
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila", numero)
        except ValueError:
            if elemento not in "+-*/%" or len(elemento) != 1:
                raise ValueError("Operando inválido")
            try:
                a1 = p.desapilar()
                print("DEBUG: desapila", a1)
                a2 = p.desapilar()
                print("DEBUG: desapila", a2)
            except ValueError:
                print("DEBUG: error pila faltan operandos")
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == "%":
                resultado = a2 % a1
            print("DEBUG: apila", resultado)
            p.apilar(resultado)
    
    res = p.desapilar()
    if p.es_vacia():
        return res
    else:
        print("DEBUG: error pila sobran operandos")
        raise ValueError("Sobran operandos")

def main():
    expresion = input("Ingrese la expresión a evaluar: ")
    elementos = expresion.split()
    print(calculadora_polaca(elementos))

if __name__ == "__main__":
    main()
