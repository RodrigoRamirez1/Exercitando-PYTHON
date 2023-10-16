# LEITURA DE DADOS ESTRUTURADOS COM A BIBLIOTECA PANDAS

import pandas as pd

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)
print(df_bancos.head())