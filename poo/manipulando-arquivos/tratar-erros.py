# erros mais comuns
# FileNotFoundError
# PermissionError
# IOError
# UnicodeDecodeError
# UnicodeEncodeError
# IsADirectoryError

try:
    file = open("aspodksa.txt", "r")
except FileNotFoundError:
    print("Arquivo não encontrado")
