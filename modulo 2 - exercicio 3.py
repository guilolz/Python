print("Comparando numeros:")
valor1 = int(input("Digite o primeiro numero:"))
valor2 = int(input("Digite o segundo numero:"))
if valor1 > valor2:
    print("O primeiro valor {} é o maior!".format(valor1))
elif valor2 > valor1:
    print("O segundo valor {} é o maior!".format(valor2))
elif valor1 == valor2:
    print("Ambos numeros {} e {} são iguais!".format(valor1,valor2))
