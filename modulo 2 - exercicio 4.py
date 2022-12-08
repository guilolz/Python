from datetime import date
ano = int(input('Ano de nascimento: '))
print('[1]MASCULINO')
print('[2]FEMININO')
sexo = int(input('Qual seu sexo: '))
idade = date.today().year - ano
if idade == 18 and sexo == 1:
    print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
    print(f'Voce tem que se alistar logo')
elif idade > 18 and sexo == 1:
    print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
    a = idade - 18
    print(f'Voce deveria ter se alistado há {a} anos')
    print(f'Seu alistamento foi em {date.today().year - a}')
elif idade < 18 and sexo == 1:
    print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
    a = 18 - idade
    print(f'Falta ainda {a} anos para voce se alistar')
    print(f'Seu alistamento sera em {date.today().year + a}')
elif sexo == 2 and idade < 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}')
    print('Você é mulher e não tem idade')
    print('Tchau')
    print('Volte daqui um tempo se você querer')
elif sexo == 2:
    print('Mulheres não precisam se alistar, fica por sua conta:')
    print('[1]Quero me alistar')
    print('[2]Não quero me alistar')
    women = int(input('Digite uma das opções: '))
    if women == 2:
        print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
        print('Então tchau')
    elif women == 1 and idade == 18:
        print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
        print('Está na hora de se alistar')
    elif women == 1 and idade > 18:
        print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
        a = idade - 18
        print(f'Você deveria ter se alistado há {a} anos.')
        print(f'Seu alistamento foi em {date.today().year - a}')
    elif women == 1 and idade < 18:
        print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
        a = 18 - idade
        print(f'Falta ainda {a} anos para você se alistar.')
        print(f'seu alistamento sera em {date.today().year + a}.')