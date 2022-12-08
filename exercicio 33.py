print("---" * 20)
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))
maior = num1
menor = num1
if num2 < num1 and num2 < num3:
    menor=num2
if num3 < num1 and num3 < num2:
    menor=num3
if num2 > num1 and num2 > num3:
    maior=num2
if num3 > num1 and num3 > num2:
    maior=num3

    print("O maior numero é: {}".format(maior))
    print("-_-" * 20)
    print("O menor numero é: {}".format(menor))
    print("-_-" * 20)

