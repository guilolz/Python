num = int(input("Digite um numero:"))
cont = 0
for i in range (2,num):
    if num % i == 0:
        print(f"O numero é divisivel por {i}")
        cont += 1
if cont == 0:
    print(f"O numero {num} é primo.")
else:
    print(f"O numero {num} não é primo")



