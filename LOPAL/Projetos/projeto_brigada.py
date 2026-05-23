#Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)

# Contexto:
# O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).

# Objetivo:
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.

#Requisitos:
# O sistema deve cadastrar os funcionários, armazenando o nome, setor e o status dos treinamentos (NR-10, NR-35 e Brigada.
# O sistema deve receber o setor do funcionário.
# O sistema deve listar a obrigatoriedade de EPIs para cada setor.
# O sistema deve criar uma função que receba o ano do último treinamento da Brigada de Incêndio.
# Exiba na tela um resumo com o total de funcionários cadastrados e quantos estão com treinamentos em dia.

import time

def cadastrar_funcionario():
    nome_cadastro = input("Digite o nome do funcionário: ")
    setor_cadastro = input("Digite o setor do funcionário e sua NR: ")
    treinamento_cadastro = input("O funcionário está com os treinamentos em dia? (sim/não): ").lower()

    return nome_cadastro, setor_cadastro, treinamento_cadastro

def verificacao_epi():
    nome_funcionario = input("Digite o nome do funcionário: ")
    setor_cadastrado = int(input("\nInforme o setor no qual o funcionário exerce seu cargo\n1-Elétrica(NR-10)\n2-Trabalho em Altura(NR-35)\n3-Brigada\n"))
    
    return setor_cadastrado, nome_funcionario

def verificar_treinamento_brigada():
    nome_funcionario = input("Digite o nome do Funcionário: ")
    ano_treinamento_funcionario = int(input("Informe o seu ultimo ano de Treinamento da Brigada de Incêncio: "))
    ano_atual = int(input("Informe o ano atual: "))
    
    return nome_funcionario, ano_treinamento_funcionario, ano_atual

def resumo_dos_funcionarios(nomes, setores, treinamentos):
    total_funcionarios = len(nomes)
    treinamentos_em_dia = 0

    for status in treinamentos:
        if status == "sim":
            treinamentos_em_dia += 1

    print("\nRelatório Geral")
    print(f"Total de funcionários cadastrados: {total_funcionarios}")
    print(f"Funcionários com treinamentos em dia: {treinamentos_em_dia}")

nomes = []
setores = []
treinamentos = []


    





while True:
    print("\n=== Sistema de Gestão de Segurança do Trabalho (SESMT) ===")
    print("1. Cadastrar Funcionário")
    print("2. Listar EPIs por Setor")
    print("3. Verificar Treinamento da Brigada de Incêndio")
    print("4. Resumo dos Funcionários")
    print("5. Encerrar")
    

    
    opcao_menu = int(input("Escolha uma opção: "))
    if opcao_menu == 1:
            print("Cadastro de Funcionário")
            nome_cadastro, setor_cadastro, treinamento_cadastro = cadastrar_funcionario()

            nomes += [nome_cadastro]
            setores += [setor_cadastro]
            treinamentos += [treinamento_cadastro]

            if treinamento_cadastro == "sim":
              print(f"Funcionário {nome_cadastro} cadastrado com sucesso no setor {setor_cadastro} com status de treinamento em dia.")

            elif treinamento_cadastro == "não":
              print(f"Funcionário {nome_cadastro} cadastrado no setor {setor_cadastro} com status de treinamento em atraso. Por favor, regularize a situação.")

            else:
              print("Opção de treinamento inválida. Por favor, responda com 'sim' ou 'não'.")


   
    elif opcao_menu == 2:
        print("\nVerificação de EPIs (NR-6)")
        setor_cadastrado, nome_funcionario = verificacao_epi()

        if setor_cadastrado == 1:
            print(f"\nNome do funcionário: {nome_funcionario}\nLista de EPIs obrigatórios para áreas de Elétrica(NR-10)\n\n-Luvas de Alta Tensão\n-Botas Dielétricas")

        elif setor_cadastrado == 2:
            print(f"\nNome do funcionário: {nome_funcionario}\nLista de EPIs obrigatórios para áreas de Trabalho(NR-35) em Altura\n\n-Cinturão de Segurança\n-Talabarte")
        
        elif setor_cadastrado ==3:
            print("Prezado Funcionário;\nEquipamentos de Proteção para área de Brigada serão debatidos em reunião\nAgradecemos a compreensão.\n")

        else: 
            print("Selecione um NR correspondente ao seu setor.")

    elif opcao_menu == 3:
        print("\nVerificação de Treinamentos da Brigada de Incêncio")
        nome_funcionario, ano_treinamento, ano_atual = verificar_treinamento_brigada()
        calculo_treinamento = ano_atual - ano_treinamento
        if calculo_treinamento >2:
            print(f"Olá {nome_funcionario}!\nTreinamento Vencido! Encaminhar para reciclagem.")
        
        else:
            print(f"Olá {nome_funcionario}!\nTreinamento Válido.")

    elif opcao_menu == 4:
        print("\nRelatório Geral")
        
        
              
        resumo_dos_funcionarios(nomes, setores, treinamentos)

        
    elif opcao_menu == 5:
        print("Encerrando Sistema...")
        for contagem_encerramento in range(3, 0, -1):
            print(f"{contagem_encerramento}")
            time.sleep(2)

        print("Sistema Encerrado.")
        break





        
