class Animal:
    nome = 'Animal'
    cabeca = 1

    def _init_(self):
       pass
 
    def viver(self):
      print('estou vivo !!')

class Cachorro(Animal):

    _DNA = 'Cachorro'

    def _init_(self, nome, idade, cor, raca, porte):
                                    # parametros obrigatorios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.porte = porte
                                # Atributos padrao para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.focinho = True
        self.lingua = True
        self.olhos = 2
        self.rabo = True
        print(f'Cachorro{nome}, Construido com Sucesso!')

                                    # O que faz - Metodos
        def latir(self):
            if self.lingua:
            print(f{self.nome}'Au Au Au')

       
        def comer(self):
            print('Comendo...')

        def cheirar(self):
            if self.focinho:
                print('Cheirando...')

        def cagar(self):
            print('Cagando...')

        def dormir(self):
            print('Dormindo...')

        def _del_(self):
            print(f'Descanse em Paz {self.nome}')

        def _str_(self):
            return 'Constroi um cachorro'
    


