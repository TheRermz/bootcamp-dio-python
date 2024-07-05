# INTERFACES DEFINEM O QUE UMA CLASSE DEVE FAZER E NÃO COMO
# PYTHON TEM INTERFACE?
# O CONCEITO DE INTERFACE É DEFINIR UM CONTRATO, ONDE SÃO DECLARADOS OS MÉTODOS(O QUE DEVE SER FEITO) E SUAS RESPECTIVAS ASSINATURAS.
# EM PYTHON UTILIZAMOS CLASSES ABSTRATAS PARA CRIAR CONTRATOS. CLASSES ABSTRATAS NÃO PODEM SER INSTANCIADAS
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # quando declaro o método abstrato eu digo que o filho tem que implementar o método
    @property
    @abstractmethod
    def marca(self): ...


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print("Desligando a TV...")

    @property
    def marca(self):
        return "Philco"


class ControleAC(ControleRemoto):
    def ligar(self):
        print("Ligando AC")

    def desligar(self):
        print("Desligando AC")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
ac = ControleAC()
ac.ligar()
ac.desligar()
print(ac.marca)
