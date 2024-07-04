# ################################################################# #
#   TODOS OS RECURSOS EM PYTHON SÃO PUBLICOS.                       #
# A CONVENÇÃO DIZ QUE RECURSOS INICIADOS COM UNDERLINE SÃO PRIVADOS #
# O INTERPRETADOR NÃO GARANTE A PROTEÇÃO DO RECURSO                 #
# ################################################################# #

class Conta:
    def __init__(self, num_agencia, saldo=0):
        self._saldo = saldo
        self.num_agencia = num_agencia


    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

conta = Conta('0001', 100)
conta.depositar(100)
conta.sacar(50)
print(conta._saldo)
