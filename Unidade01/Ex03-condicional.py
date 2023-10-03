# a = 5
# b = 10

# if a<b:
#     print("a é menor que b")
# else: 
#     print("a é maior que b")

# r=a+b
# print(r)

# ESTRUTURA ENCADEADA

codigo_produto = int(input("Digite o codigo de compra: "))

if codigo_produto == 5222:
    print("Compra a vista")
elif codigo_produto == 5333:
    print("Compra no boleto")
elif codigo_produto == 5444:
    print("Compra a proza no cartão")
else:
    print("Produto não cadastrado")