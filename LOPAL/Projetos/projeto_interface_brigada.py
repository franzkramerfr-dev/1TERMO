import tkinter as tk
from tkinter import messagebox


# LISTAS
nomes = []
setores = []
treinamentos = []


# ===================== FUNÇÕES =====================

def cadastrar_funcionario():
    nome = entry_nome.get()
    setor = entry_setor.get()
    treino = entry_treino.get().lower()

    nomes.append(nome)
    setores.append(setor)
    treinamentos.append(treino)

    if treino == "sim":
        messagebox.showinfo("Cadastro",
            f"Funcionário {nome} cadastrado com sucesso no setor {setor} com status de treinamento em dia.")

    elif treino == "não":
        messagebox.showinfo("Cadastro",
            f"Funcionário {nome} cadastrado no setor {setor} com status de treinamento em atraso. Por favor, regularize a situação.")

    else:
        messagebox.showwarning("Aviso",
            "Opção de treinamento inválida. Por favor, responda com 'sim' ou 'não'.")


def abrir_cadastro():
    global entry_nome, entry_setor, entry_treino

    janela = tk.Toplevel(app)
    janela.title("Cadastrar Funcionário")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome do funcionário:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Setor e NR:").pack()
    entry_setor = tk.Entry(janela)
    entry_setor.pack()

    tk.Label(janela, text="Treinamento em dia? (sim/não):").pack()
    entry_treino = tk.Entry(janela)
    entry_treino.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar_funcionario).pack(pady=10)


def epi():
    nome = entry_epi_nome.get()
    setor = int(entry_epi_setor.get())

    if setor == 1:
        messagebox.showinfo("EPIs",
            f"Nome do funcionário: {nome}\n\n-Luvas de Alta Tensão\n-Botas Dielétricas")

    elif setor == 2:
        messagebox.showinfo("EPIs",
            f"Nome do funcionário: {nome}\n\n-Cinturão de Segurança\n-Talabarte")

    elif setor == 3:
        messagebox.showinfo("EPIs",
            "Prezado Funcionário;\nEquipamentos de Proteção para área de Brigada serão debatidos em reunião\nAgradecemos a compreensão.\n")

    else:
        messagebox.showwarning("Aviso",
            "Selecione um NR correspondente ao seu setor.")


def abrir_epi():
    global entry_epi_nome, entry_epi_setor

    janela = tk.Toplevel(app)
    janela.title("EPIs por Setor")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome do funcionário:").pack()
    entry_epi_nome = tk.Entry(janela)
    entry_epi_nome.pack()

    tk.Label(janela, text="Setor:\n1-Elétrica(NR-10)\n2-Trabalho em Altura(NR-35)\n3-Brigada:").pack()
    entry_epi_setor = tk.Entry(janela)
    entry_epi_setor.pack()

    tk.Button(janela, text="Verificar", command=epi).pack(pady=10)


def brigada():
    nome = entry_b_nome.get()
    ano = int(entry_b_ano.get())
    atual = int(entry_b_atual.get())

    if atual - ano > 2:
        messagebox.showinfo("Brigada",
            f"Olá {nome}!\nTreinamento Vencido! Encaminhar para reciclagem.")
    else:
        messagebox.showinfo("Brigada",
            f"Olá {nome}!\nTreinamento Válido.")


def abrir_brigada():
    global entry_b_nome, entry_b_ano, entry_b_atual

    janela = tk.Toplevel(app)
    janela.title("Brigada de Incêndio")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome:").pack()
    entry_b_nome = tk.Entry(janela)
    entry_b_nome.pack()

    tk.Label(janela, text="Ano do treinamento:").pack()
    entry_b_ano = tk.Entry(janela)
    entry_b_ano.pack()

    tk.Label(janela, text="Ano atual:").pack()
    entry_b_atual = tk.Entry(janela)
    entry_b_atual.pack()

    tk.Button(janela, text="Verificar", command=brigada).pack(pady=10)


def resumo():
    total = len(nomes)
    ok = 0

    for t in treinamentos:
        if t == "sim":
            ok += 1

    messagebox.showinfo("Relatório Geral",
        f"Total de funcionários cadastrados: {total}\nFuncionários com treinamentos em dia: {ok}")


def encerrar():
    app.destroy()


# ===================== TELA PRINCIPAL (MENU) =====================

app = tk.Tk()
app.title("Sistema de Gestão de Segurança do Trabalho - SESMT")
app.geometry("1080x720")
app.configure(bg="#2c3e50")


tk.Label(app, text="MENU", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

tk.Button(app, text="Cadastrar Funcionário", command=abrir_cadastro, bg="green", fg="white").pack(pady=5)

tk.Button(app, text="Listar EPIs por Setor", command=abrir_epi, bg="blue", fg="white").pack(pady=5)

tk.Button(app, text="Verificar Brigada", command=abrir_brigada, bg="purple", fg="white").pack(pady=5)

tk.Button(app, text="Resumo dos Funcionários", command=resumo, bg="orange", fg="white").pack(pady=5)

tk.Button(app, text="Encerrar", command=encerrar, bg="red", fg="white").pack(pady=5)


app.mainloop()