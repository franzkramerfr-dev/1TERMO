#Sistema de elevador de prédio

# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de tranasportar até 5 pessoas
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa
# O elevador deve exibir mensagens indicando o andar atula, o número de pessoas no elevador, e as ações realizadas
# O programa deve continuar rodando até que o usuario dedicada encerrar.

# Requisitos Funcionais (RF):
# O elevador deve se mover para cima e para baixo
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador possui uma capacidade limite de pessoas
# O elevador deve exibir mensagens indicando o andar atula, o número de pessoas no elevador, e as ações realizadas

# Requisitos Não Funcionais (RNF):
# O elevador deve exibir mensagens indicando o andar atula, o número de pessoas no elevador, e as ações realizadas.
# O programa pode continuar rodando até que o usuario dedicada encerrar.
# O elevador pode começar do andar 0.


import time


def subir(andar_atual, numero_andar):
    print("Elevador Subindo...")

    for contagem_andar in range(andar_atual + 1, numero_andar + 1):

        print(f"Andar {contagem_andar}")
        time.sleep(2)


def descer(andar_atual, numero_andar):
    print("Elevador Descendo...")

    for contagem_andar in range(andar_atual - 1, numero_andar - 1, -1):
        
        print(f"Andar {contagem_andar}")
        time.sleep(2)


def encerrar():
    print("Encerrando Sistema.")

    for contagem_encerramento in range(3, 0, -1):
        print(f"...{contagem_encerramento}")
        time.sleep(1)


andar_atual = 0

while True:
    print("\n=== Sistema de Elevador de Prédio ===")

    numero_pessoas = int(
        input("Quantas pessoas irão utilizar o elevador?\n")
    )

    if numero_pessoas > 5:
        print("Número de pessoas acima do limite!")

    else:
        andar_usuario = input(
            "Qual andar deseja ir?\n"
            "1 | 2 | 3\n"
            "4 | 5 | 6\n"
            "7 | 8 | 9\n"
            "0 |10 |\n"
            "Digite 'sair' para encerrar:\n"
        ).lower()

        if andar_usuario == "sair":
            encerrar()
            break

        numero_andar = int(andar_usuario)

        if numero_andar > andar_atual:
            subir(andar_atual, numero_andar)

        elif numero_andar < andar_atual:
            descer(andar_atual, numero_andar)

        else:
            print("O elevador já está neste andar.")

        andar_atual = numero_andar

        print(f"Você chegou ao seu andar.")
        print(f"Andar Atual: {andar_atual}")