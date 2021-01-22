import pandas as pd 

dados = pd.read_csv("dados.csv")

'''
O resultado do corr()método é uma tabela com muitos números que representa quão bem está a 
relação entre duas colunas.

O número varia de -1 a 1.

1 significa que existe uma relação de 1 para 1 (uma correlação perfeita) e, para este conjunto 
de dados, cada vez que um valor subia na primeira coluna, o outro também subia.

0,9 também é um bom relacionamento e, se você aumentar um valor, ou outro aumentará também.

-0,9 seria um relacionamento tão bom quanto 0,9, mas se você aumentar um valor,
o outro provavelmente diminuirá.

0,2 significa NÃO um bom relacionamento, o que significa que se um valor subir não significa que o outro subirá.
'''

print(dados.corr())