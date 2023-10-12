import sqlite3

try:

    banco = sqlite3.connect('cadastros.db') #criar banco de dados

    cursor = banco.cursor() #é atraves desse cursor que vamos operar os comandos sql

    cursor.execute("DELETE from clientes WHERE idade = 30") #Deletar tabela com algumas condiçoes com WHERE

    banco.commit()
    banco.close()
    print("os dados foram removidos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)