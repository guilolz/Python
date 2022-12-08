r1 = int(input('Digite o comprimento da primeira reta:'))
r2 = int(input('Agora da segunda reta:'))
r3 = int(input('E a terceira:'))

# Verificar
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Esse triângulo NÃO EXISTE!')
# Determinar tipo de triângulo
elif r1 == r2 and r1 == r3:
    print('Esse triângulo existe e ainda por cima é um triângulo EQUILÁTERO!')
elif r1 == r2 or r1 == r3:
    print('Esse triângulo exite e ainda é um ISÓCELES!')
else:
    print('Esse é um triângulo ESCALENO!')