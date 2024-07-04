class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('parando bicicleta')
        print('bicicleta parada')

    def correr(self):
        print('vrum')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

caloi = Bicicleta('Vermelho', 'Caloi', 2022, 600)
caloi.buzinar()
caloi.correr()
caloi.parar()
