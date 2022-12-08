r = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))

if r < r2+r3 and r2 < r+r3 and r3 < r+r2:
    print("Sim é possivel fazer um triangulo com essas retas!!")
else:
    print("Não é possivel")

