#!/usr/bin/python3

#####
## Tratamento de excessões
#####
# try: # Tente
#     print('Divisão de dois valores')
#     numero1 = int(input('Digite um numero a ser divido: '))
#     numero2 = int(input('Digite outro numero a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError: # Exceção
#     print('Insira Somente numeros')
# except ZeroDivisionError as e:
#     print('Não foi possivel fazer a divisão', e)
# except Exception as e:
#     print('Erro na execução do Programa', e)
# finally:
#     print('Saindo do script')
    


#########
## Lançando exceções
#########

try:
    opcao = input('Não Digite 5: ')
    if opcao == '5':
        raise ValueError('Eu falei pra você não digitar 5')
except ValueError as e:
     print('Deu erro: ',e)


