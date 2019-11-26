#!/usr/bin/python3

#####
## Exercicio condicional composta
#####

# Criar uma variavel idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber ou não, caso possa, atribuir
# ao valor de uma variável embriagado o valor true, senão false

 idade = int(input('Digite sua idade: '))

# Criar Validação se a pessoa bebeu para atribuir a variável 
# embriagado como True ou false

# criar uma validação para elif para que se a idade for menor

if idade >= 18:
#     # If's validam se variável tem conteúdo
    habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
    if habilitacao == 'y':
        habilitacao = True
        bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
       if bebeu:
            embriagado = True
        else:
             embriagado = False
         else:
          habilitacao = False
         else:     embriagado = False

 #Criar uma validação para que se a pessoa tiver carteira de
# motorista, ela possa dirigir. Porém
# Criar condicional para que se a pessoa estiver embriagada,
# mostrar uma mensagem que ela não pode dirigir




if habilitacao and not embriagado:
     print('Você pode dirigir')
else:
     print('Você não pode dirigir')
     
######
## Condicionais aninhadas
######

nome = input('Digite o seu nome: ').strip().title()

# Consigo fazer validação em mais de um fator
# com comportamento diferente
if nome == 'Daniel':
    print(f'Seu nome é muito bonito, {nome}')
elif nome == 'Juliana':
    print(f'Seu nome é bem legal, {nome}')
    elif nome == 'Jorge':
        print(f'Seu nome é muito feio, {nome}')
else:
        print(f'Seu nome é bem normal, {nome}')