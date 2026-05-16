# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

print("Bem-vindo ao mundo da programação em Python!")

# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
print ("Seu nome é", nome)
print ("E você tem", idade)

# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

print("Bem-vindo a minha calculadora em Python!")
v1 = 135
v2 = 246
print  ("O resultado da soma 135 com 246 é:", v1 + v2)

v3= 512
v4= 128
print ("O resultado da subtração 512 menos 128 é:", v3 -v4)

val1 = float(input("Digite o primeiro valor :"))
val2 = float(input(("Digite o segundo valor : ")))
print("O resultado da conta é:", val1 + val2)

val1 = float(input("Digite o primeiro valor :"))
val2 = float(input(("Digite o segundo valor : ")))
print("O resultado da conta é:", val1 - val2)

# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

print("Bem-vindo a minha calculadora em Python!")
v1 = 15
v2 = 8
print  ("O resultado da multiplicação 135 por 246 é:", v1 * v2)


v3 = 78
v4 = 3
print  ("O resultado da divisão 135 por 246 é:", v3 / v4)

val1 = float(input("Digite o primeiro valor :"))
val2 = float(input(("Digite o segundo valor : ")))
print("O resultado da conta é:", val1 * val2)

val1 = float(input("Digite o primeiro valor :"))
val2 = float(input(("Digite o segundo valor : ")))
print("O resultado da conta é:", val1 / val2)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

print("Bem-vindo a minha calculadora em Python!")
v1 = 5
v2 = 3
print  ("O resultado de 5 elevado á 3a potencia é:", v1 ** v2)

print("Bem-vindo a minha calculadora em Python!")
val1 = float(input("Digite o primeiro valor :"))
val2 = float(input(("Digite o segundo valor : ")))
print("O resultado da conta é:", val1 ** val2)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

n1=input("Digite seu nome:")
n2=input("Digite agora seu sobrenome:")
print(n1 +" "+ n2)


# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

v1 =float(input("Informe a quantidade de peças produzidas:" ))
v2 =float(input("Informe a quantidade de peças defeituosas:"))
sub = v1 - v2
total= sub / v1
print("a taxa de aproveitamento das peças foi de", total * 100 , "%" )


# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

idade = int(input("informe sua idade:"))
var = idade + 10
print ("Você tem", idade ,"e em 10 anos terá", var )

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

n1= int(input("Quantas noites você ficaria hospedado?:"))
n2= 250 * n1
print("O custo total da viagem seria de", n2 + 412)

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.

print("===Relatório de Vendas===")
nome = input("Informe o produto:")
v1 = int(input("Informe a quantidade:"))
v2 = int(input("Qual o valor do produto?: "))
print("Valor total: R$", v1 * v2)






 
