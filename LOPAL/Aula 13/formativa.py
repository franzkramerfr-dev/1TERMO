# Exercício
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
# Calcule a idade




import tkinter as tk
from tkinter import messagebox, ttk

def cadastro_usuario():
    nome_usuario = ent_nome_usuario.get()
    idade_usuario = ent_idade_usuario.get()

    if nome_usuario and idade_usuario == "":
        messagebox.showwarning("Verificar Dados", "Verificar os campos")
    else:
        calculo_idade = 2026 - int(idade_usuario)
        messagebox.showinfo("Cadastro Realizado!", f"Bem-Vindo {nome_usuario}, você tem {calculo_idade} anos!")

        
janela = tk.Tk()
janela.title("Tela Cadastral")
janela.geometry("500x500")
janela.configure(bg= "gray")

lbl_titulo_aplicacao = tk.Label(janela, text ="Bem-vindo a tela cadastral", font=("Arial" , 14), fg = "black", bg= "white")
lbl_titulo_aplicacao.grid(row=0, column = 0, pady= 10, padx=20)

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome: ", font= ("Arial", 12), fg = "black")
lbl_nome_usuario.grid(row=1, column = 0, pady = 10, padx = 20)

lbl_idade_usuario = tk.Label(janela, text="Digite seu ano de nascimento: ", font = ("Arial", 12), fg="black")
lbl_idade_usuario.grid(row=2, column = 0, pady= 10, padx= 20)

ent_nome_usuario = tk.Entry(janela, font=("Arial", 12), fg = "black")
ent_nome_usuario.grid(row=1, column= 1, padx =20, pady= 10)

ent_idade_usuario = tk.Entry(janela, font=("Arial", 12), fg= "black")
ent_idade_usuario.grid(row= 2, column = 1, pady = 10, padx =20)

btn_enviar_dados = tk.Button(janela, text= "Calcular Idade", font=("Arial", 12), fg = "white", bg= "gray", command=cadastro_usuario)
btn_enviar_dados.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", font=("Arial", 12), width=20 , fg= "white", bg = "gray", command=janela.destroy) 
btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)




janela.mainloop()