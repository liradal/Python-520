#/usr/bin/python3

#######
## Estrutura de Condicional Simples
#######
nome = input('Digite o seu nome') .strip() . title()
sobrenome = input ('Digite o seu Sobrenome: ') .strip() . title()

#if nome == 'Daniel':
#   print('Olá Professor')
#print('Seja bem vindo')

########
## Estrutura Condicional Composta
########

# if nome == 'Daniel':
#     print(f'Bem vindo Professor {nome}')
# else:
#     print(f'Bem vindo Aluno {nome}')
# print('Você pode utilizar a Plataforma')

####
## Comparando duas condições
####

# if nome == 'Daniel' and sobrenome == 'Silva': # pode se utilizar o or
#     print(f'Bem vindo Professor {nome}')
# else:
#     print(f'Bem vindo Aluno {nome}')
# print('Você pode utilizar a Plataforma')
######
## Condicionais Encadeadas
######

if nome == 'Daniel':
    if sobrenome == 'Silva':
print('Olá Professor')
        else:
print('Voçê é Daniel, mas não é Professor')
else:
print(f'Olá Aluno {nome}')