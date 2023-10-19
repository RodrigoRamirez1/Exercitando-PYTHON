import pandas as pd

import os
current_directory = os.getcwd()
print(current_directory)


data = pd.read_csv("advertising.csv", sep=",", header=0, encoding="utf8")
# print(data.to_string())
# print(data['TV'].sum())

# print(data.head()) #exibe 5 primeiras linhas
print(data.info()) #exibe informações da tabela