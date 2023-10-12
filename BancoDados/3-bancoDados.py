#Bassando dados na tabela com variáveis

import sqlite3

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o email: ")

banco = sqlite3.connect('cadastros.db') #criar banco de dados

cursor = banco.cursor() #é atraves desse cursor que vamos operar os comandos sql

# cursor.execute("CREATE TABLE clientes (nome text, idade integer, email text)") #criar tabela

cursor.execute("INSERT INTO clientes VALUES ('"+nome+"', "+str(idade)+", '"+email+"')") #inserir registros na tabela com as variaveis

# cursor.execute("UPDATE clientes SET nome = 'Fabio' WHERE idade = 40") #Atualiza dados

banco.commit()