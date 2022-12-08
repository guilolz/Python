compra = float(input("Quanto vc pagou nesse acessorio? R$"))
desconto = compra * 0.05
total = compra - desconto
print("A sua compra de {} ficará com {:.2f} após um desconto de 5%" .format(compra,total))