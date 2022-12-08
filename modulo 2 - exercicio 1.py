valor = float(input("Digite o valor da casa:"))
print("===" * 20)
salario = float(input("Digite o seu salario:"))
print("===" * 20)
meses = int(input("Voce pretende pagar em quantos anos"))
print("===" * 20)
conta = valor / (meses * 12)
salario1 = salario * 0.30
if conta < salario:
    print("Emprestimo negado!!")
else:
    print("Para pagar uma casa de {} , será necessario pagar {} durante {}".format(valor, salario1, conta))
    print("===" * 20)
    print("Sucesso!!")
