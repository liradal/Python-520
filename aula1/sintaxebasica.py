#!/usr/bin/python3

print('Hello World')
print('Seja bem vindo')
nome = input ('Digite o seu nome: ')
print(nome)

print('Seu nome é: ' , nome)
#print(input ('Digite o seu nome: ') , 'Seja bem vindo')
#print(input ('Digite a sua Idade: ') , 'Idade')
#Tipos de variáveis

texto = '4linux' #string
numero = 3 # int
numero_real= 3.6 # float
numero_complexo = 2j # complex
CONSTANTE = 3.14 # Representação em codigo de uma constante
Booleanas = True # bool -> Vedadeiro e Falso
listas = ['item1', 'item2', 'item3'] #list
tuplas = ('item1' , 'item2') # tuple
tupla2 = 'item1' , 'item2' #tupla
dicionarios = {'nome':'Daniel','Sobrenome:':'Silva'} #dict


idade = input('Digite a sua Idade: ')
#print('Seu nome é {0}, e sua idade é {1} anos'.format(nome,idade))
print(nome,idade,sep=' ',end='\n\n')
#novos comandos
#print(texto.upper())
#print(texto.title())
#print(texto.strip())
#print(texto.replace('l','p'))

email = str(input('Digite um email: ')).lower().strip()
print(email)

#mensagem = 'Digite o seu nome: '
#nome = input(mensagem).title().strip()
#print (f'Seja bem vindo {nome}')

verdadeiro = True
falso = False

print(not(falso == True))


