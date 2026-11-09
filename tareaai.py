def validar_cadena(cadena):
    pila = []

    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for caracter in cadena:
        if caracter in "({[":
            pila.append(caracter)

        elif caracter in ")}]":
            if not pila or pila[-1] != pares[caracter]:
                return "Inválido"

            pila.pop()

    if not pila:
        return "Válido"
    else:
        return "Inválido"


# Entrada de datos
cadena = input("Ingrese una cadena de paréntesis, llaves y corchetes: ")

# Mostrar resultado
print(validar_cadena(cadena))
