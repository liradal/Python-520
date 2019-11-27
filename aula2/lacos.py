#!/usr/bin/python3

######
## laços de Repetição
######

######
## Laço Whiloe
######
# Este laço executa enquanto uma condição for verdadeira

# i = 0
# while(i < 10): # enquanto i for menor que 10
#     print(i)   # mostra valor de i
#     i += 1     # i = i + 1
# repete

# Como fazer controle de um loop while

# while(True):
#     i += 1
#     if i == 3:
#         break
#     if i == 3:
#         continue
#     print('Teoricamente, um loop infinito')

# # Continue retoma do começo a execução de um loop
# i = 100
# while i > 0: # enquanto i < 0
#     i -= 1 # i = i - 1
#     if i % 2 == 1:
#         continue
#     print(i)

#######
## Laço For
#######
# Percorre itens em determinado alcance de valores

# for (i=0;i<10;i++){
# // rotina de codigo
# }

# lista = []
# for i in range(1000): # Começa do 1 ate o 100 de 2 em 2
#     lista.append(i)
# print(lista)
# # percorrer lista
# for i in lista:
#     if i % 2 ==0:
#         print(f'\033[31m{i}\033[0m','par')
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m','impar')
# # percorrer um dicionario
# dicionario = {
#     'nome':'Daniel':
#     'Sobrenome':'Silva'
#      }
# # for i in dicionario
# # print(dicionario[i])

# for chave,valor in dicionario.itens()
#    print(chave)
#    print(valor) não funcionou

# Enumerando itens de uma lista
# lista = ['item1','item2','item3','item4','item5','item6','item7']
# print(list(enumerate(lista)))
# for indice,valor in enumerate(lista):
#     print(indice)

#     # list comprehension (compreensão de listas)
lista = [x*2 for x in range(1,100)] # aqui qualquer numero antes da virgula é o inicio
print(lista)


