import tkinter as  tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#JANELA
janela = tk.Tk()
janela.title("Formulário de Login")
janela.minsize(600,600)
janela.maxsize(600,600)
janela.geometry("600x600")
#ENTRADA DE NOME
label_entrada = ttk.Label(janela,text="Nome:")
label_entrada.place(x=10, y=25)
entrada_nome = tk.Entry(janela)
entrada_nome.place(x=10, y=50)
#ENTRADA DE SOBRENOME
label_entrada = ttk.Label(janela,text="Sobrenome:")
label_entrada.place(x=10, y=75)
entrada_sobrenome = tk.Entry(janela)
entrada_sobrenome.place(x=10, y=100)
#ENTRADA DE NASCIMENTO
label_entrada = ttk.Label(janela,text="Data de nascimento:")
label_entrada.place(x=10, y=125)
entrada_nasc = tk.Entry(janela)
entrada_nasc.place(x=10, y=150)
#ENTRADA DE CPF
label_entrada = ttk.Label(janela,text="CPF:")
label_entrada.place(x=10, y=175)
entrada_cpf = tk.Entry(janela)
entrada_cpf.place(x=10, y=200)
#ENTRADA DE CEP
label_entrada = ttk.Label(janela,text="CEP:")
label_entrada.place(x=10, y=225)
entrada_cep = tk.Entry(janela)
entrada_cep.place(x=10, y=250)
#ENTRADA DE SEXO
label_entrada = ttk.Label(janela,text="Sexo:")
label_entrada.place(x=10, y=275)
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)
opc1.place(x=10, y=300)
opc2.place(x=10, y=325)
opc3.place(x=10, y=350)
#ENTRADA DE ESTADO
label_combo = ttk.Label(janela, text="Selecione o estado:")
label_combo.place(x=10, y=375)
estado_entrada = ttk.Combobox(janela, values=["MG", "RJ", "RS", "RN", "CE"])
estado_entrada.place(x=10, y= 400)
#ENTRADA DE CIDADE
label_entrada = ttk.Label(janela,text="Cidade:")
label_entrada.place(x=10, y=425)
entrada_cidade = tk.Entry(janela)
entrada_cidade.place(x=10, y=450)
#BOTÃO
def clicar():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    nasc = entrada_nasc.get()
    cpf = entrada_cpf.get()
    cep = entrada_cep.get()
    estado = estado_entrada.get()
    if opcao.get() == 1:
        sexo = "Masculino"
    elif opcao.get() == 2:
        sexo = "Feminino"
    elif opcao.get() == 3:
        sexo = "Outro"
    cidade = entrada_cidade.get()
    messagebox.showinfo("Mensagem: ",f"Nome: {nome}, Sobrenome: {sobrenome}, Nascido em: {nasc}, CPF: {cpf}, CEP: {cep}, Sexo: {sexo}, Estado: {estado}, Cidade: {cidade}.")
btn = tk.Button(janela, text="Enviar formulário", command=clicar)
btn.place(x=20, y=475)
janela.mainloop()