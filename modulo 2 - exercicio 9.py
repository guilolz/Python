print("Pagamento das compras!!")
preço = float(input("Digite o valor das compras:"))
print("Formas de pagamento \n [1] A vista dinheiro/cheque \n [2] A vista no cartão \n [3] 2x no cartão \n [4] 3x no "
      "cartão ou mais ")
pagamento = int(input("Digite o modo que voce deseja pagar:"))

if pagamento == 1:
    desconto = preço * 0.10
    desconto = preço - desconto
    print(f"O valor a pagar será de {desconto}")
elif pagamento == 2:
    desconto = preço * 0.5
    desconto = preço - desconto
    print(f"O valor a pagar será de {desconto}")
elif pagamento == 3:
    print(f"O preço a pagar será de {preço}")
elif pagamento == 4:
    num1 = int(input("Quantas parcelas? "))
    juros = preço * 0.20
    juros = preço + juros
    parcela = juros / num1
    print(f"A parcela será de {parcela} \nE no total será pago {juros}")

