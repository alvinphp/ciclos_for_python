frase = input("dame una frase").lower() #frases y pasamos a minuscula
contador = 0
for letra in frase:
    if letra in "aeiou":
        print(letra)
# se imprimen las vocales
#  que se encuentran en una frase
# insertada por un usuario