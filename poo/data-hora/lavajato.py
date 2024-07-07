import datetime

tipo_carro = "P"  # P, M , G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_pequeno)
    print(data_atual)
    print(data_estimada)
elif tipo_carro == "M":
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_medio)
    print(data_atual)
    print(data_estimada)
else:
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_grande)
    print(data_atual)
    print(data_estimada)
