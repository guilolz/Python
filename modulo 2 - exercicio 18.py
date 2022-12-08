frase = str(input("Digite uma palavra/frase:")).lower().replace(" ", "")
inverso = frase[::-1]
if inverso == frase:
    print(f"A palavra {frase} é um palíndromo.")
else:
    print(f"A palavra {frase} não é um palíndromo.")


