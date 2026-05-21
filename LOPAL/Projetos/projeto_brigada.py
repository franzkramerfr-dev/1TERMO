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


while True:
    print("\n=== Sistema de Gestão de Segurança do Trabalho (SESMT) ===")
    print("1. Cadastrar Funcionário")
    print("2. Listar EPIs por Setor")
    print("3. Verificar Treinamento da Brigada de Incêndio")
    print("4. Resumo dos Funcionários")
    print("5. Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        def cadastrar_funcionario():
         print("Cadastro de Funcionário")
         nome_cadastro = input("Digite o nome do funcionário: ")
         setor_cadastro = input("Digite o setor do funcionário: ")
         treinamento_cadastro = input("O funcionário está com os treinamentos em dia? (sim/não): ").lower()
         return nome_cadastro, setor_cadastro, treinamento_cadastro
        funcionario = cadastrar_funcionario()
        if treinamento_cadastro == "sim":
          print(f"Funcionário {funcionario[0]} cadastrado com sucesso no setor {funcionario[1]} com status de treinamento em dia.")
   
    # elif opcao == "2":
    #     # Código para listar EPIs por setor
        
    # elif opcao == "3":
    #     # Código para verificar treinamento da Brigada de Incêndio
        
    # elif opcao == "4":
    #     # Código para exibir resumo dos funcionários
        
    # elif opcao == "5":
