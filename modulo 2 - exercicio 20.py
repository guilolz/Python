menor: float = 0
maior: float = 0
for i in range(0, 5):
    peso = float(input("Digite seu Peso:"))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f"O maior peso foi {maior}")
print(f"O menor peso foi {menor}")

