#!/usr/bin/python3 

#####
## funcoes
#####
#blocos de codigo pre definidos para execução
# def mostrar_hello_world():

    # print('hello world')
  
    # mostrar_hello_world()
    # criando uma estrutura de funções
# def menu():
#     print('Escolha a opção: ')
#     print('1- Resgistrar Produto: ')
#     print('2- Consultar Saldo de Caixa: ')
#     print('3- Abrir Caixa Registradora: ')
#     print('4- Fechamento do mês: ')
#     return input('Digite a opção desejada')
# def registrar_produto():
#     print ('Produto Registrado')
# def consultar_saldo(): 
#     print ('Saldo é R$ x') 
# def abrir_caixa():
#     print ('Abrindo')
# def fechamento():
#     print('fechando')

# while True:
#     print('Caixa Registradora')
#     opcao = menu()
#     if opcao == '1':
#         registrar_produto()          
#     elif opcao == '2':
#         consultar_saldo()         
#     elif opcao == '3':
#         abrir_caixa()         
#     elif opcao == '4':
#         fechamento()         
#     else:
#         break
#     input()





# Funções Anonimas
var = lambda x : x*2
print(var(2))

numeros = list(range(1,100))

# def dobro(x):
#     return x * 2def dobro(x):
#     return x * 2

print(list(map(lambda x : x + 3,numeros)))

