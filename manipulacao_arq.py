#!/usr/bin/python3

#########
## Manipulando arquivos com python
#########

# ### Abrir um arquivo para modificação
# #### Método não recomendado ####
# ponteiro = open('nomedoarquivo.txt','a') # abre  um ponteiro para
# # escrita de arquivos, modo utilizado é o read plus (r+) que serve para
# # leitura e escrita.Possuimos varios modos de acesso, por exemplo:
# # w = sobrescrita
# # r = somente leitura
# # + = abre um arquivo para atualização acrescenta e modifica
# # a = complemento
# # x = criação
# # esse método não é recomendado porque sempre necessita
# # ser encerrado com close, isso foi substituido com adição
# # do comando with será mostrado adiante
# ponteiro.write('Olá Mundo\n')
# ponteiro.close()


#### Método Usual #####

with open('nome do arquivo2.txt','w') as arquivo:
    arquivo.write('Olá mundo\n')
    arquivo.writelines(['banana','maça'])
        #arquivo em modo de leitura
with open('nome do arquivo2.txt','r') as arquivo:
    letras = arquivo.read()

    print(letras)
