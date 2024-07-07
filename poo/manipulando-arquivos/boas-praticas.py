from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(ROOT_PATH / "example.txt", "r") as file:
        print("Trabalhando com o arquivo")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", encoding="utf-8") as file:
        file.write("Aprendendo a manipular arquivos com Python")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
