#!/usr/bin/python3

########
## Exercicio de Funcões
########

# Criar uma função de soma que retorna a soma de 2 valores
# Criar uma função de Subtração que retorna a subtração de 2 valores
# Criar uma função de multiplicação que retorna a multiplicação de 2 valores
# Criar uma função de divisão que retorna a divisão de 2 valores
# Criar uma função que gera uma raiz quadrada de um numero x

# Como fazer documentação da sua função
def soma(n1, n2):
    ''' Função de soma

    Este modulo realiza soma com dois valores e retorna o valor.'''

    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Não tem como cara')
    else:
        return n1 / n2

def raizQuadrada(n1):
    if n1 < 0:
        #raise ValueError('Não tem como fazer isso com esse número')
        n1 **= 0.5
        return complex(n1)
    else:
        return n1 ** 0.5

n1 = input('Digite o primeiro numero: ')
n2 = input('Digite o segundo numero: ')
resultado = soma(int(n1),int(n2))
print(resultado)