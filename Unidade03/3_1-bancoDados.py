import sqlite3

conn = sqlite3.connect('aulaDB.db')
# print(type(conn))

ddl_create = """ 
CREATE TABLE fornecedor(
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
)
"""
cursor = conn.cursor()
cursor.execute(" SELECT cidade from fornecedor")
for linha in cursor.fetchall():
    print(linha)
# cursor.execute(ddl_create)
# print(type(cursor))
# print("Tabela criada!")
# print("Descrição do crusor: ", cursor.description)
# print("Linhas afetadas: ", cursor.rowcount)

# cursor.execute("""
# INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
# VALUES ('Empresa A', '11.111.11/1111-11', 'São Paulo', 'SP', '11111-111', '2023-10-11') """)

# cursor.execute("""
# INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
# VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2023-10-11') """)

# cursor.execute("""
# INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
# VALUES ('Empresa C', '33.333.333/3333-33', 'Florianópolis', 'SC', '33333-333', '2023-10-11') """)

# conn.commit()

# print("Dados inseridos!")
# print("Descrição do cursor: ", cursor.description)
# print("Linhas afetadas: ", cursor.rowcount)

cursor.close()
conn.close()