class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('Ligando o motor...')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'



class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')


moto = Motocicleta('preta', 'abc-1234', 2)


carro = Carro('Branco', 'xde-0098', 4)


caminhao = Caminhao('Roxo', 'gfd-8712', 8, True)


print(carro)
print(moto)
print(caminhao)
