"""valor_verdadeiro = True
valor_false = False

if valor_verdadeiro != False:
    print("A variável valor_verdadeiro é verdadeira")

# IF E ELSE

print ('Menu: \n2 = Escreve Talita\n2 = Escreve João\n3 = Escreve Juliana')

opcao = input('Escolha uma opção: ')

if opcao == '1':
    print("Talita")
elif opcao == '2':
    print('João')
elif opcao == '3':
    print('Juliana')
else:
    print('Opção inválida')

# UTILIZAÇÃO DE IF NOT

idade = 50

if not idade == 50:
    print('Você não tem 50 anos')
else:
    print('Você tem 50 anos')

"""

if not True:
    print('Entrou no if')
else:
    print('Entrou no else')