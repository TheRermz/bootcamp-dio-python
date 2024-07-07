# podemos usar write() ou writelines()

file = open("example.txt", "w")
file.write("Olar.")
file.writelines([" Escrevendo ", "um novo ", "texto."])
file.close
