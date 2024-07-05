class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Murilo", 1566514)
aluno_2 = Estudante("Camila", 1563244)

mostrar_valores(aluno_1, aluno_2)

print("***********************")
# a variavel escola é uma variável de classe, portanto, se alterada, altera de todos os objetos instanciados
Estudante.escola = "Python"
# a variável numero é uma variável de instancia, portanto, se alterada, ela altera apenas o objeto selecionado
aluno_1.numero = 3234345
aluno_3 = Estudante("Chappie", 3343)

mostrar_valores(aluno_1, aluno_2, aluno_3)
