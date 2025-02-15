class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self,  cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, num_patas):

        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, num_patas=num_patas )


ornitorrinco = Ornitorrinco(num_patas=2, cor_pelo='marrom', cor_bico='laranja' )
print(ornitorrinco)
