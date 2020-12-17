arquivo = open("arquivo2.txt", "a")

'''
	r = somente leitura 
	w = escrita(caso o arquivo ja exista ele apaga o antigo )
	a = leitura e escrita (adiciona novo conteudo no final do arquivo)
	r+ = leitura e escrita
	w+ = escrita (semelhante ao modo w normal)
	a+ = leitura e escrita (abre o arquivo para atualização)
'''

arquivo.write("Este é meu arquivo criado pelo python\n")

arquivo.close()