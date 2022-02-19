# Importando o SQLite
import sqlite3 as lite

# Criando conexao
conexao = lite.connect('banco_clientes.db')

# Criando a Tabela
con = conexao.cursor()

con.execute(''' CREATE TABLE clientes(
   nome text,
   sobrenome text,
   email text,
   telefone text  
)
''')

conexao.commit()
conexao.close()