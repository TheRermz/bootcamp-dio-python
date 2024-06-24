linha = "-".center(80, '-')
palavra = 'pYtHon'


print(palavra.upper())
print(palavra.lower())
print(palavra.title())
print(linha)


# cortar espaços em branco na string

palavra = '      "python" '
print(palavra.strip())
print(palavra.lstrip())
print(palavra.rstrip())
print(linha)


#juncoes e centralização

palavra = 'python'
print(palavra.center(10,'#'))
print('.'.join(palavra))

print(linha)
#interpolacao de variaveis
# 3 maneiras

#primeira --> %
nome = 'Murilo'
idade = 26
numeros = 1.256
print('%')
print('Meu nome é %s e tenho %d anos'% (nome, idade))
print('format')
print('Meu nome é {} e tenho {} anos'.format(nome, idade))
print('fstring')
print(f'Meu nome é {nome} e tneho {idade} anos')
print(f'o valor de numeros é {numeros:.2f}')
print(f'o valor de numeros é {numeros:10.2f}')
