# CÁLCULO IR POR SALÁRIO ANO DE 2023

salario = float(input("Digite o Salário: "))

if salario <= 2112.00:
    print("Colaborador isento de imposto")
    print(f"Salário a receber R$ {salario}")

elif salario <= 2826.65:
    print("Colaborador deve pagar R$158.40 de imposto")
    print(f"Salário a receber R$ {salario - 158.40}")

elif salario <= 3751.05:
    print("Colaborador deve pagar R$370.40 de imposto")
    print(f"Salário a receber R$ {salario - 370.40}")

elif salario <= 4664.68:
    print("Colaborador deve pagar R$651.73 de imposto")
    print(f"Salário a receber R$ {salario - 651.73}")

else: 
    print("Colaborador deve pagar R$884.96 de imposto")
    print(f"Salário a receber R$ {salario - 884.96}")