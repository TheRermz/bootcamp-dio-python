class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # preciso ter acesso ao contexto da classe?

    @classmethod  # sim
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod  # não
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1997, 8, 1, "Murilo")
print(Pessoa.maior_idade(18))  # True
print(Pessoa.maior_idade(17))  # False
