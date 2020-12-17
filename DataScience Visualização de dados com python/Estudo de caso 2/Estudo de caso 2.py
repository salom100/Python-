'''Este programa esta analisando o codigo genetico 
	do dna 
	Ele devera pegar pegar os dados que vem em um padrao 
	e deve pegar os pares desses padroes e ver quantos pares 
	de cada combinação existem
'''

'''PARA ANALISAR O GENOMA DO HUMANO SO SUBSTITUIMOS O ARQUIVO QUE ELE VAI ABRIR E O ARQUIVO QUE ELE IRA ESCREVER'''
entrada = open("bacteria.txt").read()# esta abrindo o arquivo onde esta a sequencia e esta lendo ele por completo
saida = open("bacteria.html","w")# cria um arquivo html aonde exibirei os dados

cont = {} # dicionario criado para os pares que vou captalizar

# Estes 2 FORs tem como objetivo pegar os valores e jogar no dicionario
for i in ['A','T','C','G','N']:
	for j in ['A','T','C','G','N']:
		cont[i+j]=0

# o replace esta trocando o pular linha por nada para que nao ocorra erro na hora da leitura
entrada = entrada.replace("\n","")

# este for esta analisando os pares percorrendo todos os caracteres menos o ultimo 
for k in range(len(entrada)-1):
	cont[entrada[k]+entrada[k+1]] +=1 # pra cada par ele coloca um +1 e assim ele vai contando os pares

print(cont) #printa o que foi capturado


'''SESSAO HTML 
	O codigo abaixo passara a frequencia que os pares aparecem imprindo na cor RGBA sen oque o unico valor a ser alterado sera o de Alpha
	para isso ele faz a divisao da quantidade dos pares pelo maior numero de pares que ha 
	assim ele obtem o resultado dentro do intervalo de 0 e 1 que é o intervalo de ALPHA
	apos isso salvamos no arquivo html uma sequencia de divs sendo que cada bloco representa um par

'''

i=1 # usado para fazer a quebra de linha
for k in cont:  # for que fara a produção de cada quadrado 
	transparencia = cont[k]/max(cont.values()) # calcula o alpha que iremos inserir
	saida.write("<div style='width:100px; border:1px solid #111; color:green; height:100px; float:left; background-color:rgba(0,0,0,"+str(transparencia)+"')>"+k+"</div> ") # escrevendo no arquivo passando as divs 

	if i%5 == 0: # a cada 5 blocos ele pula uma linha
		saida.write("<div style='clear:both'></div>")
	i+=1
saida.close()















