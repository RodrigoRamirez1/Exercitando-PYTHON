# LEITURA COM JSON E CSV

import pandas as pd
out1 = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
print(out1)

out2 = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()
print(out2)