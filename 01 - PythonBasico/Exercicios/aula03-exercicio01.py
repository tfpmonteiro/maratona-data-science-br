print('##### INSCRIÇÃO PARA O EXERCÍCITO #####')

nome = input('Informe seu nome completo: ')
nascimento = int(input('Informe o ano do seu nascimento: '))
peso = input('Informe o seu peso: ')
altura = float(input ('Infome a sua altura: '))

nascimento = 2018 - nascimento;
peso_float = float(peso)

if nascimento > 18 and peso_float >= 60 and altura >= 1.70:
    print('Parabéns', nome, "você esta apto(a) para ingressar no exercícito!")
else:
    print('Infelizmente você não atende aos requisitos para ingressar no exercícito.')
