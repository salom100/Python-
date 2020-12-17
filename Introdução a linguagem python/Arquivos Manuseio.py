arquivo = open("arquivo.txt")
linhas = arquivo.readlines()
print("UTILIZANDO A FUNÇÂO READLINES \n")
print(linhas)
'''
imprimir linha por linha
for linhas in linhas:
	print(linhas)
'''
print("\nUTILIZANDO A FUNÇAO READ\n")
arquivo1 = open("arquivo.txt")
todo_conteudo = arquivo1.read()
print(todo_conteudo)