#!/usr/bin/env python3
import random 

class Humano:
    # #atributos
    # pernas = 2
    # bracos = 2
    # cabeca = 1
  _PI = 3.1415
  # metodos magicos
def _init_(self, nome):     #metodo construtor
   # atributos de objeto
   self.pernas = 2
   self.braco = 2
   self.nome = nome  
   self.saldo = 0         
  # metodo
def acidente(self):
   self.pernas -= 1
   def saldo_bancario(self):
        if self.perrnas < 2 and self.nome == 'Carlos':
           self.saldo -= 10000
           print('Voce esta de ferias permanente')
        if random.randint(1,10) == 9:
               self.saldo *= -1
        else:
                print('Voce não é Carlos, beleza')
                self.saldo += 1000
                print(f'voce agora tem {self.saldo}')

carlos = Humano('Carlos')        # criando um objeto
# carlos._PI = 4                 # acessando um atributo
# print(carlos._PI)              # mudando um
# print(Humano._PI)
print(carlos.pernas)
carlos.acidente()
print(carlos.pernas)
carlos.saldo_bancario()
print(carlos.saldo)