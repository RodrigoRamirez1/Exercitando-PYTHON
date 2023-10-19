import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'turma':['A', 'B', 'C'],
    'qtde_alunos':[33, 50, 45]
    }

df = pd.DataFrame(dados)
df.plot(x='turma', y='qtde_alunos', kind='bar')
