import tkinter as  tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#JANELA
janela = tk.Tk()
janela.title("Formulário de Login")
janela.configure(background="#FFFFFF")
janela.minsize(400,250)
janela.maxsize(400,250)
janela.geometry("400x250")
#ENTRADA DE USUÁRIO
label_entrada = ttk.Label(janela,text="Usuário:")
label_entrada.place(x=10, y=25)
label_entrada.configure(background="#FFFFFF")
entrada = tk.Entry(janela)
entrada.place(x=10, y=50)
#ENTRADA DE SENHA
label_entrada = ttk.Label(janela,text="Senha:")
label_entrada.place(x=10, y=75)
label_entrada.configure(background="#FFFFFF")
entrada = tk.Entry(janela)
entrada.place(x=10, y=100)
#BOTÃO
def clicar():
    messagebox.showinfo("Mensagem: ","Usuário logado com sucesso!")
btn = tk.Button(janela, text="Enviar formulário", command=clicar)
btn.place(x=20, y=130)
#IMAGEM
imagem = tk.PhotoImage(file="iconelogin.png")
imagem = imagem.subsample(4,4)
tk.Label(janela, image=imagem).place(x=150, y=10)


janela.mainloop()