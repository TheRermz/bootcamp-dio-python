# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:


# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:

def recomendar_plano(consumo):

    plano_recomendado = ''

    if consumo < 10:
       plano_recomendado +=  f'Plano Essencial Fibra - 50Mbps'
    elif consumo < 20:
        plano_recomendado += f'Plano Prata Fibra - 100Mbps'
    else:
        plano_recomendado += f'Plano Premium Fibra - 300Mbps'
    return plano_recomendado

# Solicita ao usuário que insira o co nsumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
