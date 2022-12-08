idade2 = 0
media = 0
velho: str = 0
cont = 0
maior = 0
for i in range(0, 4):
    nome = str(input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu sexo(M ou F)".upper()))
    idade2 += idade
    if maior < idade:
        velho = nome
    if sexo == 'M' and 'm':
        if maior < idade:
            velho = nome
    if sexo == 'F' and 'f':
        if idade < 20:
            cont += 1
media = idade2 / 5
print(f"A media de idade é {media}")
print(f"O homem mais velho é :{velho}")
print(f"A quantidade de mulheres com menos de 20 anos é: {cont}")



