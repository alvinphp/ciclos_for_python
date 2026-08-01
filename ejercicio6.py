frase = input("dame una frase").lower()
contador = 0
for letra in frase:
    if letra in "aeiou":
        contador = contador + 1
        print(contador)
    # cuenta la cantidad de vocales
    # que hay en una frase

    