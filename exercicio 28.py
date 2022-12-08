import random
from time import sleep
print("---" * 20)
num = random.randrange(0,5)
print("Vou sortear um numero entre 0 e 5 tente adivinhar!!")
print("---" * 20)
escolha = int(input("Qual numero será sorteado pelo computador? "))
print("Processando...")
sleep(5)
if escolha == num:
    print("Acertou")
else:
    print("--Errou--")
    print("Numero sorteado foi {}".format(num))




