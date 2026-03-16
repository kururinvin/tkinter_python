import tkinter as tk
#Criação da janela e definição de tamanho.
janela_main = tk.Tk()

janela_main.title("Aphelios do LoL")
janela_main.configure(background="#4800CE")
janela_main.minsize(200,200)
janela_main.maxsize(1000,1000)
janela_main.geometry("300x300")

#Objetos na janela.
tk.Label(janela_main,
         text="Esse é o aphelios, campeão do lol olha 👇",
         bg="#4800CE",
         font=("Arial", 20, "bold")
         ).pack()
imagem = tk.PhotoImage(file="abbbb.png")
imagem = imagem.subsample(1,1)
tk.Label(janela_main, image=imagem).pack()




janela_main.mainloop()