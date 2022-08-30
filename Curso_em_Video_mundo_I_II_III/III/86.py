class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

nome = input('digite seu nome: ')
sexo = input('digite seu sexo: ')
cpf = input('digite seu cpf: ')
if __name__ == "__main__":
    pessoa1 = pessoa = [nome, sexo, cpf]
    print(pessoa.cpf,  pessoa.sexo, pessoa.nome)
