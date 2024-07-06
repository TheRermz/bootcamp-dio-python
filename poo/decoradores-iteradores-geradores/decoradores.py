# funções são objetos de primeira classe
# ou seja, eu posso pasar uma função dentro de uma função


import functools


def dizer_oi(nome):
    print("2.Executando dizer_oi")
    return f"oi {nome}"


def incentivar_aprender(nome):
    print("2.Executando incentivar_aprender")

    return f"Oi {nome}, vamos aprender Python!"


def mensagem(func_mensagem, nome):
    print("1.Executando mensagem")

    return func_mensagem(nome)


print(mensagem(incentivar_aprender, "Murilo"))
print(mensagem(dizer_oi, "Ediberto"))

# inner function


def pai():
    print("Escrevendo da pai()")

    def filho1():
        print("Escrevendo da filho1()")

    def filho2():
        print("Escrevendo da filho2()")

    filho1()
    filho2()


pai()

# retronar funções dentro de funções


def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair


resultado = calcular("+")(1, 3)
print(resultado)

# decorador simples


def meu_decorador(func):
    def envelope():
        print("Faz algo antes de executar a função")
        func()
        print("Faz algo depois de executar a função")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


# ola = meu_decorador(ola_mundo)

# ola()

ola_mundo()

# decorador com argumentos


def segundo_decorador(func):
    def envelope(*args, **kwargs):
        print("fazendo algo antes")
        func(*args, **kwargs)
        print("fazendo algo depois")

    return envelope


@segundo_decorador
def olar_morlo(nome):
    print(f"olar {nome}")


olar_morlo("Murilo")


# retornar valor decorado


def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        # func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope


@duplicar
def aprender(tech):
    print(f"estou aprendendo {tech}")
    return tech.upper()


r = aprender("python")
print(r)
