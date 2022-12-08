from datetime import date
print("Classificação de idade para natação:")
nascimento = int(input("Digite o seu ano de nascimento:"))
ano = idade = date.today().year - nascimento
print("A sua idade é de {} anos".format(ano))
if ano <= 9:
    print("Classificaçao: Mirim")
elif ano <= 14:
        print("Classificação: Infantil!!")
elif ano < 19:
    print("Classificação: Junior!!")
elif ano <= 25:
    print("Classificação: Senior!!")
elif ano >= 25:
    print("Classificação: Master!!")