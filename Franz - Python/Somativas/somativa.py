# Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"
print("===Registro de Veículo===")
modelo = input("Informe o modelo do veículo: \n")
placa = input("Informe a placa: \n")
print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio.
print("Cálculo de Autonomia")
v1 = float(input("Informe a capacidade do tanque de combustível em litros:"))
v2 = float(input("Informe o consumo médio do caminhão: "))
km = v1*v2
print(f"Distância total que o veículo pode percorrer com o tanque cheio: {km}km")

# Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.

print("Conversor de Moeda (Frete Internacional)")
valor_frete = float(input("Valor de frete em Dolar: "))
conversao_real = float(input("Valor da taxa em Reais: "))
total_conversao = valor_frete * conversao_real
print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversao_real} e o total do frete {total_conversao:.2f}")


# Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.
print("===Média de Entrega===")
temp1= float(input("Informe o tempo de entregas (em horas) da primeira rota: "))
temp2= float(input("Informe o tempo de entregas (em horas) da segunda rota: "))
temp3= float(input("Informe o tempo de entregas (em horas) da terceira rota: "))
média = temp1+ temp2+ temp3
total= média/3
print(f"A média de entrega foi de: {total} horas")

# Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

print("===Monitor de Carga===")
peso= float(input("Informe o peso atual do caminhão em toneladas: "))
if peso <=10:
    print("Carga Leve")
elif 10 < peso < 25:
    print("Carga padrão")
else: 
    peso >=25
    print("ALERTA: Excesso de Peso!")

# Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".

print("===CLASSIFICADOR DE DESTINO===")
print("Regiões conforme a primeira letra: ")
print("S: Região Sul ")
print("N: Região Norte")
print("Outros: Internacional")
code = str(input("Insira o código da carga: "))
if code == "N":
    print("Região Norte")
elif code == "S":
    print("Região Sul")
else:
    print("Região Internacional")

# Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

print("===LIBERAÇÃO DE SAÍDA===")
checklist = input("O checklist foi realizado (Concluído ou Não Concluído)")
motorista = input("O motorista foi identificado (Sim ou Não)")
#and = verdadeiro
#or = verdadeiro ou falso
if checklist == "Concluído" and  motorista == "Sim":
    print("Iniciar Rota - Boa Viagem ")
else: 
    print("Voltar e realizar o Checklist! ")

# Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# print("===CÁLCULO DE ATRASOS===")
# total_entregas = int(input("Informe o total de entregas agendadas: "))
# entregas_atraso = int(input("Informe o total de entregas realizadas com atraso: "))
# total = entregas_atraso / total_entregas

# if total >0.10:
#     print("Necessário Otimizar Rotas")
# # else:   
# #     print("Logística Eficiente")

# # Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# # ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# print("===VALIDAÇÃO DE CALIBRAGEM===")
# psi: 0
# v1 = float(input("Informe a medida da pressão em PSI dos pneus: "))
# if v1 <=100:
#     print("Pressão abaixo do recomendado.")
# elif v1 >=110:
#     print("Pressão acima do recomendado.")
# else:
#     print("Pressão recomendada dentro do padrão.")

# # 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# # até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
# print("===CONTAGEM REGRESSIVA PARA O FECHAMENTO DO PORTÃO===")
# from time import sleep
# for i in range(5,0,-1):
#     sleep(1)
#     print(i)
# print("Portão Trancado!")

# # 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# # vários pedidos.
# # ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# # acumulado.
# print("===Somatório de Fretes (Acumulador)===")
# faturamento = 0
# while True:
#    valor=  float(input("Informe o valor do Frete dos produtos (Digite 0 para finalizar):"))
#    if valor == 0:
#       break
#    faturamento += valor
# print(f"Faturamento total: R$ {faturamento}")

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.
# var = 0
# print("===MONITORAMENTO DE FROTA===")
# vei1= int(input("Informe a quilometragem do veículo 1: "))
# for km in range(2,6):
#     veis=  float(input(f"Informe a quilometragem do veículo {km} registrada:"))
#     if veis > var:
#         var=var+veis
    
# print(f"A maior quilometragem foi de: {var}")



# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".

negado =0
while negado != 3:
    
    var= str(input("Digite o código de acesso do rastreador:"))
    if var != "track99":
        negado= negado+1
        print("Acesso Negado!")
        print("Rastreamento Bloqueado")
    elif var:
        print("Acesso Liberado!")
        break   
        


# 14.Gerenciador de Combustível: Comece com um tanque de 500 litros. Crie um
# menu (while) onde o usuário pode: (1) Abastecer o tanque da base, (2) Retirar
# combustível para um caminhão ou (3) Sair.
tanque =500
while True:
    print("1 - Abastecer tanque")
    print("2 - Retirar combustível")
    print("3 - Sair")
    opção = input("Escolha uma opção:")
    
    if opção =="1":
        qtd = float(input("Quantos litros deseja adicionar?: "))
        tanque += qtd

    elif opção == "2":
        qtd = float(input("Quantos litros deseja retirar? "))
        tanque -= qtd 

    elif opção == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")

print(f"Tanque atual: {tanque} litros")

if tanque < 50:
    print("Reserva Crítica!")