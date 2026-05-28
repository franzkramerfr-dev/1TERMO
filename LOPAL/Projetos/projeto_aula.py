import tkinter as tk
from tkinter import messagebox

# 1. Configurar Evento

def solicitar_informacoes():
    # .get() serve para buscar o texto que foi digitado
    nome_usuario =campo_nome.get()
    idade_usuario =campo_idade.get()

    if nome_usuario =="":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
    
    if idade_usuario =="":
        messagebox.showwarning("Aviso", "Por favor, digite sua idade.")
    else:
        messagebox.showinfo("Saudações Querido aluno",  f"Olá, {nome_usuario} Idade: {idade_usuario} anos. Seja bem-vindo ao mundo das interfaces gráficas.")


# 2. Configuração de Janela
app = tk.Tk()
app.title("Página de Usuário")
app.geometry("300x300")
app.configure(bg = "#1e29be")

# 3. Componentes
lbl_nome_usuario = tk.Label(app, text= "Digite seu nome: ").grid(row= 0, column=0, padx=10, pady=10) #grid -posicionamento em grade

# lbl_nome_usuario.pack(pady = 50)

campo_nome = tk.Entry(app, font=("Arial", 12))
campo_nome.grid(row =2, column= 0, padx=10, pady=10)
# campo_nome.pack(pady =20 )

lbl_idade_usuario = tk.Label(app, text= "Digite sua idade: ").grid(row= 0, column=0, padx=10, pady=10) #grid -posicionamento em grade

# lbl_idade_usuario.pack(pady=50)

campo_idade = tk.Entry(app, font=("Arial", 12))
campo_idade.grid(row =3, column= 0, padx=10, pady=10)
# campo_idade.pack(pady=20)





btn_cadastrar = tk.Button(app, text= "Cadastrar", font =("Arial", 12, "bold"), bg=("#2ed973"), fg= "white" , command = solicitar_informacoes)
btn_cadastrar.grid(row =4, column= 0, padx=10, pady=10)
# btn_cadastrar.pack(padx= 5)

btn_fechar =tk.Button (app, text="Fechar", font=("Arial", 12, "bold"), command=app.destroy)
btn_fechar.grid(row =5, column= 0, padx=10, pady=10)

# btn_fechar.pack(pady=100)





# 4. Rodar Interface
app.mainloop()