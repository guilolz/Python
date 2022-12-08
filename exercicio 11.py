largura = float(input("Largura da parede:"))
altura = float(input("Altura da parede"))
area = largura * altura
tinta = area / 2
print("Sua parede tem {} de altura e {} de largura, sendo que a area é {}m2" .format(altura, largura, area))
print("A quantidade de tinta que vc ira utilizar para pintar toda a parede será de {}l" .format(tinta))
