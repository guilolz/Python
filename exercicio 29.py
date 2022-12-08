velocidade = float(input("Qual foi a velocidade do carro:"))
print("---" * 20)
if velocidade > 80:
    m= velocidade-80
    g= m*7
    print("O seu carro passou por {}Km, portando receberá uma multa que ficará em {}R$".format(velocidade,g))
    print("---" * 20)

else:
    print("Nada")
    print("---" * 20)


