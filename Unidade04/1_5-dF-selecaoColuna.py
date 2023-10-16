# SELEÇÃO DE COLUNAS EM UM DATAFRAME()

import pandas as pd

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)
df_uma_coluna = df_dados['idades']

print(type(df_uma_coluna))
print('Média de idades = ', df_uma_coluna.mean())
print(df_uma_coluna)

###############################################################
colunas = ['nomes', 'cpfs']

df_duas_colunas = df_dados[colunas]

print(type(df_duas_colunas))
print(df_duas_colunas)