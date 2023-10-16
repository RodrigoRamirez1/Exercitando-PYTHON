# UTILIZANDO {SERIES()}

import pandas as pd

criando = pd.Series(data=5) # Cria uma Series com o valor a
print(criando)

###########################################################################
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
saida1 = pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes
print(saida1)

###########################################################################
dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}
saida2 = pd.Series(dados) # Cria uma Series com um dicionário
print(saida2)

###########################################################################
cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
pd.Series(lista_nomes, index=cpfs)

###########################################################################
series_dados = pd.Series(lista_nomes, index=cpfs)
print(series_dados)
print(series_dados.loc['111.111.111-11'])
