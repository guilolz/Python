salario = float(input("Digite seu salario:"))
if salario > 1.250:
    aumento = salario * 0.15
    print("O seu novo salario sofreu um aumento!")
    total = aumento + salario
    print("Seu novo salario será de : {}R$".format(total))
else:
    aumento = salario * 0.10
    print("Seu salario sofreu um aumento!")
    total = aumento + salario
    print("Seu novo salario será de : {}R$".format(total))