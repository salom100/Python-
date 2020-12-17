a= "Salomon"
b= "Abasto"
c= "Macias"

concatenar=a+" "+b+" "+c+"\n" 
print("Usando a concatenação de strings eu posso somar algumas palavras como vemos em \n"+concatenar)
#Len conta a quantidade de letras que há dentro de uma certa variavel (ele conta tambem os espaços)
tamanho = len(concatenar)
print("\nPrintando a quantidade de letras caracteres que ha na variavel concatenar, o resultado é igual a:",tamanho)

print ("\nPrintando uma letra especifica da variavel A que contem salomon dentro, e a busca é = "+a[3])
print ("\nPrintando as letras atraves de um intervalo determinado como no exemplo abaixo: \n"+concatenar[5:15])

''' String é um objeto na linguagem python o que quer dizer que ele tem metodos, veremos agora alguns deles'''
print("\nA PARTIR DE AGORA USAREMOS OS METODOS QUE STRING OFERECE:")
print("Palavra normal sem o uso dos metodos = "+concatenar)
print("Metodo upper que deixa todas as letras em maiusculo = "+concatenar.upper())
print("Metodo lower que deixa todas as letras em minusculo = "+concatenar.lower())
print("Metodo que remove caracteres especiais como no caso o pular linha = "+concatenar.strip())

'''O metodo split é usado quando eu quero converter uma string em uma lista, partindo do que eu quero usar como base para separar os itens dela
	No caso a cada espaço ela deve criar um novo item na lista'''
print("\n USANDO O METODO SPLIT PARA FAZER UMA STRING VIRAR UMA LISTA")
string= "O rato roeu a roupa do rei de Roma"
print("Normal= "+string)
stringLista= string.split(" ")
print("Com Split= ",stringLista)

print("\n USANDO O METODO FIND PARA ENCONTRAR A POSIÇAO QUE SE ENCONTRA DETERMINADA PALAVRA")
'''Quando ele nao encontra a palavra ele retorna -1'''

busca = string.find("roupa")
print(busca)
print("Printando o que vem a seguir depois da palavra que eu encontrei = "+string[busca:])

print("\nUSANDO A FUNÇAO REPLACE\n")
string=string.replace("a roupa","o vestido")
print("Substituindo roupa por vestido = "+string)