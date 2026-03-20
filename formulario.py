import tkinter as  tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")

label_entrada = ttk.Label(janela,text="Nome:")
label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()
#CHECKBOX
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os termos",variable=checkbox)
check.pack()
#OPÇÃO
opcao = tk.IntVar()

opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)
opc1.pack()
opc2.pack()
opc3.pack()
#Listbox
lista = tk.Listbox(janela)
label_visoes = ttk.Label(janela, text="Selecione uma visão de genshin: ")
label_visoes.pack()
lista.insert(1, "Pyro")
lista.insert(2, "Hydro")
lista.insert(3, "Cryo")
lista.insert(4, "Geo")
lista.insert(5, "Anemo")
lista.insert(6, "Electro")
lista.insert(7, "Dendro")
lista.pack()
#Combobox
label_combo = ttk.Label(janela, text="Selecione o estado:")
label_combo.pack()
combo =ttk.Combobox(janela, values=["MG", "RJ", "RS", "RN", "CE"])
combo.pack()
#BOTÃO
def clicar():
    messagebox.showinfo("Mensagem: ","Formulário criado com sucesso!")
btn = tk.Button(janela, text="Enviar formulário", command=clicar)
btn.pack()

janela.mainloop()