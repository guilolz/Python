dias=int(input("Quantidade de dias alugado:"))
km=float(input("Quantidade de Km rodado pelo carro:"))
pagar1 = dias*60
pagar2 = km*0.15
total = pagar1+pagar2
print("O total a pagar é {}".format(total))

