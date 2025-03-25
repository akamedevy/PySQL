import tkinter

janela = tkinter.Tk()
janela.title("Voucher turma 140")
janela.geometry("400x400")

def mudar_texto():
    frase.config(text="40 days and 40 nights")

frase = tkinter.Label(janela, text="Clique no botão abaixo")
frase.pack(pady=25)

botao = tkinter.Button(janela,text="Clique aqui", command=mudar_texto)
botao.pack(pady=25)

janela.mainloop() # mantener la janiela abierta