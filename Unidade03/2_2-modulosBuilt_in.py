# ALGUNS MÓDULOS BUILT-IN 

# ---- { random() }
import random

print(random.randint(0, 100))
print(random.choice([1, 10, -1, 100]))
print(random.sample(range(100000), k=12))


# ----- { OS }
import os

os.getcwd()
os.listdir()
os.cpu_count()
os.getlogin()
os.getenv(key='path')
os.getpid()

# ----- { RE }
import re

string = 'meuArquivo_20-01-2020.py'
padrao = "[a-zA-Z]*"

texto1 = re.search(padrao, string).group()
texto2 = re.match(padrao, string).group()
texto3 = re.split("_", string)[0]

print(texto1)
print(texto2)
print(texto3)

# ---- { DATETIME }
import datetime as dt

# Operações com data e hora

hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)

uma_semana_atras = hoje - dt.timedelta(weeks=1)
agora = dt.datetime.now()
duas_horas_atras = agora - dt.timedelta(hours=2)

# Formatação
hoje_formatado = dt.datetime.strftime(hoje, "%d-%m-%Y")

#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
ontem_formatado = dt.datetime.strftime(ontem, "%d de %B de %Y")

# Converção de string para data
data_string = '11/06/2019 15:30'
data_dt = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M")