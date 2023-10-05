# ----------------   ALGORITMOS DE BUSCA {IN / NOT IN }  ---------------------

nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()

print('Marcela' in nomes)
print('Roberto' in nomes)

# --------------- BUSCA LINEAR -------------------

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

import random
lista = random.sample(range(1000), 50)

print(sorted(lista))
executar_busca_linear(lista, 10)

# [52, 73, 95, 98, 99, 103, 123, 152, 158, 173, 259, 269, 294, 313, 318, 344, 346, 348, 363, 387, 407, 410, 414, 433, 470, 497, 520, 530, 536, 558, 573, 588, 620, 645, 677, 712, 713, 716, 720, 727, 728, 771, 790, 801, 865, 898, 941, 967, 970, 979]

##################################################

# vogais = 'aeiou'

# resultado = procurar_valor(lista=vogais, valor='a')

# if resultado != None:
#     print(f"Valor encontrado na posição {resultado}")
# else:
#     print("Valor não encontrado")

# ----------------- BUSCA BINÁRIA  ---------------------

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
    return False # Se chegar até aqui, significa que o valor não foi encontrado

lista = list(range(1, 50))

print(lista)

print('\n',executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))





