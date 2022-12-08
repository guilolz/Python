print("---" * 20)
km = float(input("Digite a distancia que vc irá percorrer em Km: "))
print("---" * 20)
if km < 200:
    custo = km * 0.50
    print("O custo será de: {}R$".format(custo))
    print("---" * 20)
else:
    custo = km * 0.45
    print("O custo será de: {}R$".format(custo))
    print("---" * 20)

