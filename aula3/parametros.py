#!/usr/bin/python3

''' Parametros Python - Titulo

Esta aula analisamos como criar e documentar funções '''
######
## parametros de função 
######

# def retorna_pessoa(nome, idade=99):
#     print(f'Nome: {nome}\nidade: {idade}')

# retorna_pessoa(nome='Lira',idade=51)

### Especificar tipo de parâmetro e retorno

# Anotações de função
# def retorna_valor_int(inteiro : int, booleano : bool) -> int:
# ''' Função com anotação de tipo 

# se refere a função que possui tipos específicos e 
# mostram na sua sintaxe de construção o que é necessário ,
# sempre tem que pular uma linha '''

# inteiro = int(inteiro)
# return int(inteiro)

# print (retorna_valor_int())


# args e kwargs
# print('olá','mundo','','','','Prazer','sou','Lira')

### Criando uma Função que recebe multiplos valores
# def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
#     print(parametros_estaticos,'parametro estatico')
#     print(argumento_variavel)
    # Fazendo acesso aos parametros
    # for argumento in argumento_variavel:
    #     print(argumento)

# funcao_multi_valores('valor estatico obrogatorio',
# 'Lira','Andressa','joão','Ana',
# 'Paula','Lucas','Xuxa','Ines')

## Argumentos com Palavra chave - kwargs

# def parametros_chave_valor(**dados):
#     if dados['nome'] == 'Jose':
#         print('Acesso Negado')
#         else:
#     print('Permitido')

#Execução - método 1
# print('Método 1')
# parametros_chave_valor(nome='Jose',sobrenome='Lira',
#                         idade='51',sexo='Masculino')
# Execução- Métodp 2

# dados_requisicao = {'nome':'Jose',
#                     'sobrenome': 'Lira',
#                      'Profissão':'TSM'}
# parametros_chave_valor(**dados_requisicao)

# Decoradores de funcão
# uma função que modifica o valor de outra

# declara uma função com uma variavel função obrigatoria
def mudaCor(retorno_funcao):
    def modificaAzul(funcao):
        return f'\033[94m{retorno_funcao}\033[0m'
    return modificaAzul

@mudaCor
def log(texto):
    return texto

    print(log('Oi'))

