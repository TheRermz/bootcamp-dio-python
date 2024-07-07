# ler conteúdo do arquivo de uma vez
file = open("example.txt", "r")
# print(file.read())
for line in file:
    print(f"for line in file:\n {line}")

# for line in file.readline():
#     print(f"for line in file.readline():\n {line}")

# for line in file.readlines():
#     print(f"for line in file.readlines():\n {line}")

# while len(line := file.readline()):
#     print(line)

file.close()
