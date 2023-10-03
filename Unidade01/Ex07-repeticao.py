# RANGE / BREAK / CONTINUE

# for x in range(5):
#     print(x)

# disciplina = 'Linguagem de programação'

# for c in disciplina:
#     if c == 'a':
#         break 
#         continue
#     else:
#         print(c)

# -------------------------------------------------------

texto = '''A inserção de comentários no código do programa é uma prática normal. Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas. O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado'''

for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}' encontrada, na posição {i}")
    
    else: 
        continue
