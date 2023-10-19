# CRIANDO TABELA COM DATAFRAME

import pandas as pd

pessoas_df = pd.DataFrame({
    'Nome': ['Rodrigo', 'Ramon', 'Pandora'],
    'Idade': [27, 32, 1],
    'Peso': [75.1, 63.5, 4.2],
    'Humano': [True, True, False]
})

# print(pessoas_df.shape)

pessoas_df.rename(columns={ # renomiando as colunas [com return original]
    'Nome': 'Name',
    'Idade': 'Age',
    'Peso': 'Weight',
    'Humano': 'Human'
}, inplace=True)
# print(pessoas_df)

pessoas_df.columns = ['NAME', 'AGE', 'WEIGHT', 'HUMAN'] # RENOMIANDO DE UMA VEZ, PARA TABELAS COM POUCAS COLUNAS
# print(pessoas_df)

pessoas_df_copy = pessoas_df['AGE'].copy()
# print(pessoas_df_copy)

pessoas_df['AGE'] = 30 #atribui valor constante na coluna 'AGE'
pessoas_df['AGE'] = pessoas_df_copy #valtando para os valores originais
print(pessoas_df)