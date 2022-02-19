from tkinter import *
import sqlite3 as lite
import pandas as pd

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#257549"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#4186d7"   # azul
co7 = "#ba432e"   # vermelha
co8 = "#39da90"   # + verde
co9 = "#1787f7"   # sky blue
c10 = "#f1f2f6"   # Cinza
c11 = "#ecf1f4"   # cinza Claro
c12 = "#26985d"   # Verde claro
c13 = "#26985d"   # Verde
fundo="#f2f3f4"
novo="#abb2b9"
salvar="#58d68d"
editar="#34495e"
closer="#f80b0b"

## Funçoes para cadastrar os clientes
def cadastrar_cliente():
    # Criando conexao
    conexao = lite.connect('clientes.db')

    # Criando a Tabela
    con = conexao.cursor()
    con.execute("INSERT INTO clientes VALUES( :nome, :sobrenome, :email, :telefone)",
                {
                    'nome' :entry_nome.get(),
                    'sobrenome':entry_sobrenome.get(),
                    'email':entry_email.get(),
                    'telefone':entry_telefone.get()
                }

                )

    conexao.commit()
    conexao.close()


    # Limpar os campos depois que Cadastrar
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


def exportar_clientes():
    conexao = lite.connect('clientes.db')

    # Criando a Tabela
    con = conexao.cursor()

    con.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = con.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'id_banco'])
    clientes_cadastrados.to_csv('clientes.csv', encoding='utf8', index=False)


    conexao.commit()
    conexao.close()


## Criando uma Janela
janela = Tk()

# Title
janela.title("Cadastro de Clientes ")

# Tamanho da Janela
janela.geometry("450x450")

# Redimisionamento
janela.resizable(width=False, height=False)

# Cor de fundo
janela.config(bg=fundo)

# Labels
label_nome = Label(janela, width=10, height=2, text="Nome: ", font=('Arial 12  bold '), fg='#34495e', bg=fundo)
label_nome.grid(row=0, column=0, pady=10)

label_sobrenome = Label(janela, width=10, height=2, text="Sobrenome: ", font=('Arial 12 bold'), fg='#34495e', bg=fundo)
label_sobrenome.grid(row=1, column=0 , pady=10 )


label_email = Label(janela, width=10, height=2, text="E-mail: ", font=('Arial 12  bold '), fg='#34495e', bg=fundo)
label_email.grid(row=2, column=0, pady=10)

label_telefone = Label(janela, width=10, height=2, text="Telefone: ", font=('Arial 12  bold '), fg='#34495e', bg=fundo)
label_telefone.grid(row=3, column=0, pady=10)


# Entry

entry_nome = Entry(janela, width=40, text="Nome: ", font=('Arial 10  bold '), fg='#34495e', bg=fundo)
entry_nome.grid(row=0, column=1, pady=10)

entry_sobrenome = Entry(janela, width=40, text="Sobrenome: ", font=('Arial 10 bold'), fg='#34495e', bg=fundo)
entry_sobrenome.grid(row=1, column=1 , pady=10 )


entry_email = Entry(janela, width=40, text="E-mail: ", font=('Arial 10  bold '), fg='#34495e', bg=fundo)
entry_email.grid(row=2, column=1, pady=10)

entry_telefone = Entry(janela, width=40, text="Telefone: ", font=('Arial 10  bold '), fg='#34495e', bg=fundo)
entry_telefone.grid(row=3, column=1, pady=10)

# Button
btn_cadastrar = Button(janela, width=10, height=2, text="Cadastar Cliente", relief="flat", font=("Arial 12"), fg="#fff" , bg=c13, command = cadastrar_cliente)
btn_cadastrar.grid(row=4, column=1, padx=10, pady=10, columnspan=2, ipadx=80)

btn_exportar = Button(janela, width=10, height=2, text="Exportar Clientes", relief="flat", font=("Arial 12"), fg="#fff" , bg=editar, command = exportar_clientes)
btn_exportar.grid(row=5, column=1, padx=10, pady=10, columnspan=2, ipadx=80)

janela.mainloop()