import sqlite3

banco = sqlite3.connect('cadastros.db') #criar banco de dados

cursor = banco.cursor() #é atraves desse cursor que vamos operar os comandos sql

# cursor.execute("CREATE TABLE clientes (nome text, idade integer, email text)") #criar tabela

cursor.execute("INSERT INTO clientes VALUES ('Ramon', 32, 'ramon_123@gmail.com')") #inserir registros na tabela

banco.commit()

# cursor.execute("SELECT * from clientes") #verificar os dados inseridos 
# print(cursor.fetchall())




