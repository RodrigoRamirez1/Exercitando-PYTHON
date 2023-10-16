# CRIANDO DATAFRAME()
import pandas as pd

# ----------- CRANDO COM LISTAS --------------------------------------------------------
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

out1 = pd.DataFrame(lista_nomes, columns=['nome'])

out2 = pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas

out3 = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])

print(out1)
print("##########################################################")
print(out2)
print("##########################################################")
print(out3)
print("##########################################################")

# ------------- CRIANDO COM DICIONARIOS ------------------------------------------------
dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

out4 = pd.DataFrame(dados)
print(out4)