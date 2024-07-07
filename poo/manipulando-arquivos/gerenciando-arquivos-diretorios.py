import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# criar um diretório
# os.mkdir(ROOT_PATH / "marcos")

file = open("old.txt", "w")
os.rename("old.txt", f"roberto.txt")
file.close()

file = open("unwanted.txt", "w")
os.remove("unwanted.txt")
file.close()

shutil.move(ROOT_PATH / "roberto.txt", ROOT_PATH / "marcos" / "roberto.txt")
