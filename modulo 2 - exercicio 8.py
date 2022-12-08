print("Calculando o seu peso ideal")
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
imc = peso / (altura*altura)
print("O seu imc é de {:.3f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5 <= imc < 25:
    print("Peso ideal!")
elif 25.0 <= imc <= 30.0:
    print("Sobrepeso!!")
elif 30 <= imc <= 40.0:
    print("Obesidade!!!")
elif imc > 40:
    print("Obesidade Mórbida!!!")
