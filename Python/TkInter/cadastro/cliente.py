import mysql.connector


from tkinter import *
from tkinter import messagebox, ttk

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cliente_tk"
)

cursor = conexao.cursor()

janela = Tk()
janela.title("tkinter com mysql")
janela.geometry("600x400")

# labels e inputs de entrada

Label(janela, text="ID").grid(row=0, column=0, padx=5, pady=5)
id = Entry(janela, state=DISABLED, width=5)
id.grid(row=0, column=1, padx=5, pady=5)

Label(janela, text="Nome").grid(row=1, column=0, padx=5, pady=5)
nome = Entry(janela, width=30)
nome.grid(row=1, column=1, padx=5, pady=5)


Label(janela, text="Email").grid(row=2, column=0, padx=5, pady=5)
email = Entry(janela, width=30)
email.grid(row=2, column=1, padx=5, pady=5)

Label(janela, text="Telefone").grid(row=3, column=0, padx=5, pady=5)
telefone = Entry(janela, width=30)
telefone.grid(row=3, column=1, padx=5, pady=5)

#Listar Clientes

tabela = ttk.Treeview(janela, columns=("ID", "Nome", "Email", "Telefone"), show="headings")

tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Nome")
tabela.heading("Email", text="Email")
tabela.heading("Telefone", text="Telefone")

tabela.column("ID", width=30)
tabela.column("Nome", width=150)
tabela.column("Email", width=150)
tabela.column("Telefone", width=150)

tabela.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

cursor.execute("SELECT * FROM cliente")
for row in cursor.fetchall():
    print(row)
    tabela.insert("", END, values=row)

# funções

def cadastrar():
    nome_cliente = nome.get()
    email_cliente = email.get()
    telefone_cliente = telefone.get()

    if nome and email and telefone:
        cursor.execute("INSERT INTO cliente (nome_cliente, email_cliente, telefone) values (%s, %s, %s)", (nome_cliente,email_cliente,telefone_cliente))

        conexao.commit()

        print("cadastrou")


        nome.delete(0, END)
        email.delete(0, END)
        telefone.delete(0, END)

        tabela.insert("", END, values=(cursor.lastrowid, nome_cliente, email_cliente, telefone_cliente))

    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos")


btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=4, column=0, padx=5, pady=5)

# funções

janela.mainloop()