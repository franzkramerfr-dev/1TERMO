#Tkinter

#Componentes Principais: 

# tk : A janela
# Label: Texto em rótulo
# Button: Um botão de clique
# Entry: Um campo de entrada de texto

#Biblioteca
import tkinter as tk
from tkinter import messagebox

# 1. Criar Janela Principal
janela = tk.Tk() #Cria uma janela
janela.title("Minha Primeira Janela em GUI") # GUI - Interface Gráfica
janela.geometry("1080x720") #Determina a resolução #Largura x Altura
janela.configure(bg ="#5427CD") # Determinando o fundo da Página


# 2. Criar a função que o botão irá executar (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão! :)")


# 3. Criar os componentes (Widgets)
lbl_titulo = tk.Label(janela, text = "Bem vindo à aula de Tkinter!", font=("Arial" , 14, "bold"), bg="#4db34d")
lbn_mensagem = tk.Label(janela, text= "Aprendendo a usar o Tkinter", font=("Arial", 15, "bold"), bg = "#2de319", fg = "black")
btn_clique = tk.Button(janela, text = "Clique aqui :)" , font =("Arial", 12, "bold" ), bg= "#2DE319", fg = "white", command=mostrar_mensagem) 
#background (cor de fundo) fg(cor da fonte).


# 4. Posicionar Componentes
lbl_titulo.pack(pady = 20,) 
#pack (ativa o componente) pady (posiciona vertical) padx (posiciona horizontal)
btn_clique.pack(padx=50)
lbn_mensagem.pack(pady=50)

# 5. Rodar o loop da interface
janela.mainloop()

