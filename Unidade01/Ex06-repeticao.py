# FOR /

nome = input("Digite um nome: ")

# for c in nome:
#     print(c)

for i, c in enumerate(nome):
    print(f"Posição = {i} - Valor = {c}")