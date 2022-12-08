maior = 0
menor = 0
for i in range(1,7+1):
    idade = int(input("Digite o ano de seu nascimento:"))
    if 2022 - idade < 18:
        menor += 1
    else:
        maior += 1

print(f"{maior} Pessoas são maiores de idade")
print(f"{menor} Pessoas são maiores de idade")