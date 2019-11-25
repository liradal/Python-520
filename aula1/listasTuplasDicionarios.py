#!/usr/bin/python3  

# #contagem de lista começa sempre do 0 
# lista = ['arroz', 'feijão','Óleo','sal','açucar','temperos','sabão em pó'] 
# #           0         1       2     3       4         5         6

# #vetores multidimensionais
# lista3d = [
#     [2,3,4,5],
#     [3,4,5,6],
#     [7,5,7,8]
# ]
# #Adicionar um item no final da lista 
# lista.append('carne')

# #Adicionar um item em determinado indice da lista caso contrario indice 0
# lista.insert(4,'sabão em pó')
# print(lista)

# #remove o elemento pelo id
# lista.pop(4)

# #ordena a lista em ordem alfabetica/numerica
# lista.sort()

# #reverte a ordem da lista
# lista.reverse()

# #mostra quantidade de elementos
# print(len(lista))

# #procura o primeiro indice da ocorrencia
# print(lista.index('açucar'))

# #conta a quantidade de x no array matriz
# print(lista.count('arroz'))

# #remove o primeiro indice encontrado com o seguinte valor
# lista.remove ('sabão em pó')
# print(lista)

# #sobreescreve o elemnto em determinado indice
# lista[3] = 'maçã']
# print(lista)

# ###########
# ## Tuplas
# ###########

# #primeiro metodo para criar tuplas
# tupla = ('maçã','banana','laranja','abacaxi','uva')
# print(type(tupla))

# #segundo metodo para criar tuplas
# tupla2 = 'valor', 2,True,2j


# #acessando indices de uma tupla
# print(tupla[3])
# print(tupla[1:4])
# print(tupla[-2])

# #converter tupla para lista 
# lista_de_tupla = list(tupla)
# print(type(lista_de_tupla))

# print(tupla)

# tupla = (['indice 1'],'nome')
# tupla[0].append('indice 2')
# print(tupla)


# ##########
# ### Dicionários
# ##########

# #Criando um Dicionário
# apresentações = {
#     'Paulista' : 'Salve',
#     'Carioca' : 'Vai Flamengo',
#     'Pirata' : 'Argh',
#     'Mineiro' : 'Pão de queijo',
#     'Acre' : 'Barulhos de Dinossauro',
# }

# #Acessando indices em um dicionário
# print(apresentações['Paulista'])

# #criando um dicionário com multi valores
# linguagem_favorita = {
#     'Daniel': {
#         'Linguagem' :'Python',
#         'Tempo_de_Experiência' : '5'
#     },
#     'Olimpio': {
#         'Linguagem' : 'R',
#         'Linguagem2' : 'VBA',
#         'Tempo_de_Esperiência': '10',
#    }
# }

# print(linguagem_favorita.get('Daniel'))
# #acesso a todas as chaves
# print(linguagem_favorita.keys())
# #acesso aos valores
# print(linguagem_favorita.values())
# #acesso aos itens
# print(valores.itens())

# ##########
# ###Numeros
# ##########

#operações matematicas
somar = 2 + 2
print(2 + 2, 'Retornando o valor 2 + 2')
print(somar, 'Retornando o somar')

subtrair = somar - 2 #somar retorna um tipo inteiro
print(subtrair, 'Retornando o subtrair')

multiplicar = subtrair * 3 #subtrair retorna tambem um inteiro
print(multiplicar, 'Retornando o Multiplicar')

divisao = multiplicar / 5 #multiplicar tambem retorna um tipo inteiro
print(divisao, 'Retornando o dividir') #  retorna um ponto flutuar

potencia = 2**2
print(potencia, 'Retornando o valor da potencia')
raiz = 2 ** 0.5
print(raiz, 'Retornando o valor da raiz')

letras = 'abcdefghijk' + 'lmnopqrstuvwxyz'
print(letras,[])
