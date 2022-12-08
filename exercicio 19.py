import random
nome1 = str(input("Digite seu nome:"))
nome2 = str(input("Digite seu nome:"))
nome3 = str(input("Digite seu nome:"))
lista = [nome1,nome2,nome3]
print("O escolhido foi {}" .format(random.choice(lista)))