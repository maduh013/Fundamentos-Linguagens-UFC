Exemplo de Domínio: Personagens de um jogo

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print(f"{self.nome} atacou!")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} deu um golpe com força {self.forca}!")

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self):
        print(f"{self.nome} lançou uma magia com {self.mana} de mana!")

# Teste
g = Guerreiro("Arthur", 100, 80)
m = Mago("Merlin", 70, 150)

g.atacar()
m.atacar()
