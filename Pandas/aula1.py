import pandas as pd

Dados = {
    'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

Tabela = pd.DataFrame(Dados)
print(Tabela)