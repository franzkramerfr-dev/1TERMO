import tkinter as tk
from tkinter import messagebox, ttk

# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# def registrar_operador():
#     nome_operador = ent_nome_usuario.get()
#     turno_operador = cmb_turno.get()

#     if nome_operador == "" or turno_operador == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         messagebox.showinfo("Registro Realizado!", f"Operador {nome_operador} registrado no {turno_operador}. Boa jornada!")

# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("500x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text ="Registro de Operador", font=("Arial" , 14), fg = "black", bg= "white")
# lbl_titulo_aplicacao.grid(row=0, column = 0, pady= 10, padx=20)

# lbl_nome_usuario = tk.Label(janela, text="Digite o nome do operador: ", font= ("Arial", 12), fg = "black")
# lbl_nome_usuario.grid(row=1, column = 0, pady = 10, padx = 20)

# lbl_turno = tk.Label(janela, text="Selecione o turno: ", font= ("Arial", 12), fg = "black")
# lbl_turno.grid(row=2, column = 0, pady = 10, padx = 20)

# cmb_turno = ttk.Combobox(janela, values=["Turno A", "Turno B", "Turno C"], state="readonly", width=20)
# cmb_turno.grid(row=2, column=1, pady=10, padx=10)

# ent_nome_usuario = tk.Entry(janela, font=("Arial", 12), fg = "black")
# ent_nome_usuario.grid(row=1, column= 1, padx =20, pady= 10)

# btn_enviar_dados = tk.Button(janela, text= "Registrar Operador", font=("Arial", 12), fg = "white", bg= "green", command=registrar_operador)
# btn_enviar_dados.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", font=("Arial", 12), width=20 , fg= "white", bg = "red", command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# def calcular_producao():
#     quantidade_pecas = ent_quantidade_pecas.get()

#     if quantidade_pecas == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         producao_turno = int(quantidade_pecas) * 8
#         messagebox.showinfo("Cálculo Realizado!", f"Em um turno de 8 horas, serão produzidas {producao_turno} peças!")

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("900x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text ="Cálculo de Produção", font=("Arial" , 14), fg = "black", bg= "white")
# lbl_titulo_aplicacao.grid(row=0, column = 0, pady= 10, padx=20)

# lbl_quantidade_pecas = tk.Label(janela, text="Digite a quantidade de peças produzidas em 1 hora: ", font= ("Arial", 12), fg = "black")
# lbl_quantidade_pecas.grid(row=1, column = 0, pady = 10, padx = 20)

# ent_quantidade_pecas = tk.Entry(janela, font=("Arial", 12), fg = "black")
# ent_quantidade_pecas.grid(row=1, column= 1, padx =20, pady= 10)

# btn_calcular_producao = tk.Button(janela, text= "Calcular Produção", font=("Arial", 12), fg = "white", bg= "green", command=calcular_producao)
# btn_calcular_producao.grid(row=2, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", font=("Arial", 12), width=20 , fg= "white", bg = "red", command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=2, column=1, pady=10, padx=10)


# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.
# def converter_psi():
#     pressao_bar = ent_pressao_bar.get()

#     if pressao_bar == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         pressao_psi = float(pressao_bar) * 14.5
#         messagebox.showinfo("Conversão Realizada!", f"{pressao_bar} Bar equivale a {pressao_psi:.2f} PSI.")

# janela = tk.Tk()
# janela.title("Conversor de Unidade")
# janela.geometry("500x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text ="Conversor de Unidade", font=("Arial" , 14), fg = "black", bg= "white")
# lbl_titulo_aplicacao.grid(row=0, column = 0, pady= 10, padx=20)

# lbl_pressao_bar = tk.Label(janela, text="Digite a pressão em Bar: ", font= ("Arial", 12), fg = "black")
# lbl_pressao_bar.grid(row=1, column = 0, pady = 10, padx = 20)

# ent_pressao_bar = tk.Entry(janela, font=("Arial", 12), fg = "black")
# ent_pressao_bar.grid(row=1, column= 1, padx =20, pady= 10)

# btn_calcular_psi = tk.Button(janela, text= "Converter para PSI", font=("Arial", 12), fg = "white", bg= "green", command=converter_psi)
# btn_calcular_psi.grid(row=2, column=0, pady=10, padx=10)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", font=("Arial", 12), width=20 , fg= "white", bg = "red", command=janela.destroy) 
# btn_fechar_aplicacao.grid(row=2, column=1, pady=10, padx=10)

# janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# def calcular_media():
#     nota1 = cmb_nota1.get()
#     nota2 = cmb_nota2.get()
#     nota3 = cmb_nota3.get()

#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         media_notas = (int(nota1) + int(nota2) + int(nota3)) / 3
#         messagebox.showinfo("Média Calculada!", f"A média das peças é de: {media_notas:.2f}")

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("720x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(text= "Informe a nota de cada peça abaixo", font =("Arial", 14), bg= "white", fg= "black")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# lbl_nota1 = tk.Label (text= "Nota da Peça 1 ", font=("Arial", 12,),bg="white")
# lbl_nota1.grid(row=1, column=0, pady=10,padx=20)

# lbl_nota2 = tk.Label (text= "Nota da Peça 2 ", font=("Arial", 12,),bg="white")
# lbl_nota2.grid(row=2, column=0, pady=10,padx=20)

# lbl_nota3 = tk.Label (text= "Nota da Peça 3 ", font=("Arial", 12,),bg="white")
# lbl_nota3.grid(row=3, column=0, pady=10,padx=20)

# cmb_nota1 = ttk.Combobox(values=[0,1,2,3,4,5,6,7,8,9,10], state="readonly", width=20)
# cmb_nota1.grid(row=1, column=1, pady=10, padx=10)

# cmb_nota2 = ttk.Combobox(values=[0,1,2,3,4,5,6,7,8,9,10], state="readonly", width=20)
# cmb_nota2.grid(row=2, column=1, pady=10, padx=10)

# cmb_nota3 = ttk.Combobox(values=[0,1,2,3,4,5,6,7,8,9,10], state="readonly", width=20)
# cmb_nota3.grid(row=3, column=1, pady=10, padx=10)

# btn_calcular_media = tk.Button(text = "Calcular Média Simples", font=("Arial", 12), bg="green", command=calcular_media)
# btn_calcular_media.grid(row=4, column=0, pady=20, padx=20)

# btn_fechar_aplicacao = tk.Button(text="Fechar Aplicação", font=("Arial", 12), width=20 , bg = "red", command=janela.destroy)
# btn_fechar_aplicacao.grid(row=4, column=1, pady=20, padx=20)

# janela.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# def verificar_temperatura():
#     try:
#         temperatura_motor = int(ent_temperatura_motor.get())
#     except ValueError:
#         messagebox.showwarning("Verificar dados", "Por favor, insira um valor numérico para a temperatura.")
#         return
#     except Exception as e:
#         messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
#         if temperatura_motor == "":
#             messagebox.showwarning("Verificar dados", "O campo não pode estar vázio.")
#     else:
#         if temperatura_motor <40:
#             messagebox.showwarning("Verificação Temperatura","Baixa Carga")
#         elif 40 < temperatura_motor <70:
#             messagebox.showwarning("Verificação Temperatura", "Carga Normal")
#         else:
#             messagebox.showerror("Verificação Temperatura", "ALERTA: Resfriamento Ativado!")


# janela = tk.Tk()
# janela.title("Termostato")
# janela.geometry("700x600")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text="Sistema de Termostato", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# lbl_temperatura_motor = tk.Label(janela, text = "Informe a temperatura atual do motor em ºC", font=("Arial", 12), bg="white")
# lbl_temperatura_motor.grid(row=1, column=0, pady=10, padx=20)

# ent_temperatura_motor = tk.Entry(janela, font=("Arial", 12), bg="white", width=5)
# ent_temperatura_motor.grid(row=1, column=1)

# btn_verificar_temperatura = tk.Button(janela, text="Confirmar", font=("Arial", 12), bg="green", command=verificar_temperatura)
# btn_verificar_temperatura.grid(row=2, column=0, pady=10, padx=20)

# btn_fechar_aplicacao = tk.Button(janela, text="Fechar Aplicação", font=("Arial", 12), bg="red", command= janela.destroy)
# btn_fechar_aplicacao.grid(row=2, column=1, pady=10, padx=20)

# janela.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# def classificar_lote():
#     codigo_produto =cbm_codigo_produto.get().lower()

#     if codigo_produto == "":
#         messagebox.showerror("Verificar Dados", "Informe a Inicial do código")
#     else:
#         if codigo_produto == "a":
#             messagebox.showinfo("Classificação de Lote", "Alimentos")
#         elif codigo_produto == "e":
#             messagebox.showinfo("Classificação de Lote", "Eletrônicos")
#         elif codigo_produto != "a" and codigo_produto != "e":
#             messagebox.showinfo("Classificação de Lote", "Desconhecido")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("500x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text="Classificador de Lotes", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# lbl_codigo_produto = tk.Label(janela, text="Digite o código do produto: ", font=("Arial", 12), bg="white")
# lbl_codigo_produto.grid(row=1, column=0, pady=10, padx=20)

# cbm_codigo_produto = ttk.Combobox(janela, font=("Arial", 12), state="readonly")
# cbm_codigo_produto['values'] = ("A", "E", "Outro" )
# cbm_codigo_produto.grid(row=1, column=1, pady=10, padx=20)

# btn_classificar = tk.Button(janela, text="Classificar", font=("Arial", 12), bg="green", command=classificar_lote)
# btn_classificar.grid(row=2, column=0, pady=10, padx=20)

# btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="red", command=janela.destroy)
# btn_fechar.grid(row=2, column=1, pady=10, padx=20)

# janela.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# def verificar_seguranca():
#     sensor_porta = cmb_sensor_porta.get()
#     botao_emergencia = cmb_botao_emergencia.get()

#     if sensor_porta == "" or botao_emergencia == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         if sensor_porta == "Fechada" and botao_emergencia == "Desligado":
#             messagebox.showinfo("Segurança de Operação", "Máquina pode iniciar.")
#         else:
#             messagebox.showerror("Segurança de Operação", "ALERTA: a Máquina não pode iniciar!")

# janela = tk.Tk()   
# janela.title("Segurança de Operação")
# janela.geometry("500x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text="Inicializar Máquina", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)        

# lbl_sensor_porta = tk.Label (janela, text="Porta da Máquina: ", font=("Arial", 12), bg="white")
# lbl_sensor_porta.grid(row=1, column=0, pady=10, padx=20)

# lbl_botao_emergencia = tk.Label (janela, text="Botão Emergência: ", font=("Arial", 12), bg="white")
# lbl_botao_emergencia.grid(row=2, column=0, pady=10, padx=20)

# cmb_sensor_porta = ttk.Combobox(janela, font=("Arial", 12), state="readonly")
# cmb_sensor_porta['values'] = ("Fechada", "Aberta")
# cmb_sensor_porta.grid(row=1, column=1, pady=10, padx=20)

# cmb_botao_emergencia = ttk.Combobox(janela, font=("Arial", 12), state="readonly")
# cmb_botao_emergencia['values'] = ("Ligado", "Desligado")
# cmb_botao_emergencia.grid(row=2, column=1, pady=10, padx=20)

# btn_verificar = tk.Button(janela, text="Verificar", font=("Arial", 12), bg="green", command=verificar_seguranca)
# btn_verificar.grid(row=3, column=0, pady=10, padx=20)

# btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="red", command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=10, padx=20)

# janela.mainloop()   

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# def calcular_descarte():
#     total_pecas = ent_total_pecas.get()
#     total_defeituosas = ent_total_defeituosas.get()

#     if total_pecas == "" or total_defeituosas == "":
#         messagebox.showwarning("Verificar Dados", "Verifique os campos")
#     else:
#         try:
#             total_pecas = int(total_pecas)
#             total_defeituosas = int(total_defeituosas)
#             taxa_descarte = (total_defeituosas / total_pecas) * 100

#             if taxa_descarte > 5:
#                 messagebox.showwarning("Cálculo de Descarte", f"Taxa de Descarte: {taxa_descarte:.2f}%. Revisar Processo.")
#             else:
#                 messagebox.showinfo("Cálculo de Descarte", f"Taxa de Descarte: {taxa_descarte:.2f}%. Processo Otimizado.")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para o total de peças e defeituosas.")

# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("800x400")
# janela.configure(bg="white")

# lbl_titulo_aplicacao = tk.Label(janela, text="Insira os dados para cálculo de descarte", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# lbl_total_pecas = tk.Label(janela, text="Informe o total de peças produzidas: ", font=("Arial", 12), bg="white")
# lbl_total_pecas.grid(row=1, column=0, pady=10, padx=20)

# lbl_total_pecas = tk.Label(janela, text="Informe o total de peças defeituosas: ", font=("Arial", 12), bg="white")
# lbl_total_pecas.grid(row=2, column=0, pady=10, padx=20)

# ent_total_pecas = tk.Entry(janela, font=("Arial", 12), bg="white", width=5 )
# ent_total_pecas.grid(row=1, column=1, pady=10, padx=20)

# ent_total_defeituosas = tk.Entry(janela, font=("Arial", 12), bg="white", width=5 )
# ent_total_defeituosas.grid(row=2, column=1, pady=10, padx=20)

# btn_calcular = tk.Button(janela, text="Calcular", font=("Arial", 12), bg="green", command=calcular_descarte)
# btn_calcular.grid(row=3, column=0, pady=10, padx=20)

# btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="red", command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=10, padx=20)

# janela.mainloop()

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# def validar_medida():
#     medida_peca = ent_medida_peca.get()

#     if medida_peca == "":
#         messagebox.showwarning("Verificar Dados", "Verifique as medidas da peça")
#     else:
#         try:
#             medida_peca = float(medida_peca)
#             if 9.8 <= medida_peca <= 10.2:
#                 messagebox.showinfo("Validação de Medida", "A peça está dentro da tolerância.")
#             elif medida_peca < 9.8:
#                 messagebox.showwarning("Validação de Medida", "A peça está abaixo da tolerância.")
#             else:
#                 messagebox.showwarning("Validação de Medida", "A peça está acima da tolerância.")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a medida da peça.")

# janela = tk.Tk()
# janela.title("Sistema de Medida")
# janela.geometry("500x500")
# janela.configure(bg= "white")

# lbl_titulo_aplicacao = tk.Label(janela, text="Validação de Medida", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# lbl_medida_peca = tk.Label(janela, text="Digite a medida da peça em mm: ", font=("Arial", 12), bg="white")
# lbl_medida_peca.grid(row=1, column=0, pady=10, padx=20)

# ent_medida_peca = tk.Entry(janela, font=("Arial", 12), bg="white", width=5)
# ent_medida_peca.grid(row=1, column=1, pady=10, padx=20)

# btn_validar = tk.Button(janela, text="Validar", font=("Arial", 12), bg="green", command=validar_medida)
# btn_validar.grid(row=2, column=0, pady=10, padx=20)

# btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="red", command=janela.destroy) 
# btn_fechar.grid(row=2, column=1, pady=10, padx=20)

# janela.mainloop()

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import time

# def iniciar_prensa():
#     for contagem in range(0,10):
#         messagebox.showinfo("Contagem Regressiva", f"Contagem Regressiva: {10 - contagem} segundos restantes")
#     time.sleep(1)
    
# janela= tk.Tk()
# janela.title("Setup")
# janela.geometry("500x500")
# janela.configure(bg="white")

# lbl_titulo_aplicacao = tk.Label (text="Inicialização da Prensa", font=("Arial", 14), bg="white")
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=10, padx=20)

# btn_iniciar_prensa = tk.Button(janela, text="Iniciar Contagem Regressiva", font=("Arial", 12), bg="green", command=iniciar_prensa)
# btn_iniciar_prensa.grid(row=1, column=0, pady=10, padx=20)

# btn_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="red", command=janela.destroy)
# btn_fechar.grid(row=1, column=1, pady=10, padx=20)

# janela.mainloop()