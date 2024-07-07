import datetime

d = datetime.date(2024, 12, 1).strftime("%d/%m/%Y")
today = datetime.date.today()
now = datetime.datetime.now()
time = datetime.time(1, 10, 32)
print(d)
print(today)
print(now)
print(time)
print("##########")
# criando data e hora
d = datetime.datetime.now()
print(f"HOJE => {d}")
# adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(f"DAQUI UMA SEMANA => {d}")
