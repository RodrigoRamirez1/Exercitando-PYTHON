# USANDO AND/OR/NOT

faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if faltas <= 5 and media_final >= 7:
    print("Aluno Aprovado!")
else:
    print("Aluno reprovado")