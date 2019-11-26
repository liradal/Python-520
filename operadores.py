#!/usr/bin/python3

#########
###Operadores Aritméticos
#########

#variáveis por nomenclatura podem ter no
# máximo 16 caracteres
num1 = 6 # Número 1
num2 = 8 # Número 2
adição = num1 + num2 #adição
subtracão = num1 - num2 #subtração
multiplicação = num1 * num2 #multiplicação
divisão = num1 / num2 #Divisão
result_div_int = num1 // num2 #Resultado de uma divisão inteira
resto_div_int = num1 % num2 #Resto de uma divisão inteira (Módulo)

#Operadores de Forma Abreviada
#Pega o valor atual do numero e realiza um cálculo
#Atribuindo o resultado a variável
numero = 1
numero += 3 # 1+3          numero = numero + 3 
numero -= 3 # 4-3          numero = numero - 3
numero *= 4 # 1 * 4        numero = numero * 4
numero /= 2 # 4 / 2        numero = numero / 2
numero //= 2 # 2 // 2 = 1   numero = numero // 2
numero %= 2 # 2 % 2 = 0    numero = numero % 2

#######
### Operadores Relacionais
#######

# Operadores Relacionais servem para comparação entre fatores
# Retorna Valores Booleanos (True e False)
numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2) # Igualdade False
print(numero1 != numero2) # Diferenciação True
print(numero1 < numero2)  # Menor que True
print(numero1 <= numero2) # Menor Igual True 
print(numero1 > numero2)  # Maior que False
print(numero1 >= numero2) # Maior Igual False

print(numero1 is numero3) # Compara se estão no mesmo 
                          # Bloco de Memória True

