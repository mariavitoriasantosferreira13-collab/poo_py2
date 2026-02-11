#criando uma classe
class pessoa:

#criando um método construtor(é executado quando criamos o objeto)    


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#método pra mostrar os dados

    def apresentar(self):
        print(f"Olá, meu nome é: {self.nome}")
        print(f"olá, a minha idade é: {self.idade}")

#criando um objeto(uma pessoa)
p1 = pessoa("Maria", 17)

#chamar método
p1.apresentar()

#teste