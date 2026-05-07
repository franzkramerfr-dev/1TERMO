total_vagas =500
vagas_disponiveis =500
vagas_ocupadas = total_vagas - vagas_disponiveis
horario_chegada = None


print("===Sistema de controle de Estacionamento (Shopping Center)===")

while True:

   print("Menu de opções:")
   print("1- Entrar no estacionamento")
   print("2- Sair do estacionamento")

   escolha_menu = int(input("Digite o número da opção escolhida:\n"))
   
   if escolha_menu == 1:
      
      print("Bem vindo ao Shoppinh Center!")
     
      escolha_entrada = str(input("Informe qual maneira deseja entrar:\n1- Via Tag\n2- Via Ticket\n"))

      if escolha_entrada == "1":
       status_tag = str(input("A Tag está ativa? (Sim/Não):")).strip().lower()

       if status_tag == "sim":
        tag_id = input("Digite o ID da Tag:\n")
        horario_chegada= float(input("Informe seu horário de chegada:\n"))
        
        print("Levantando cancela...")
        import time
        time.sleep(3)
        print("Acesso liberado!")
      
       elif status_tag == "nao" or status_tag == "não":
         print("Ative sua Tag para liberar o acesso e tente novamente.")
         
       
      
      elif escolha_entrada == "2":
        
        if vagas_disponiveis >0:
           import time
           time.sleep(2)
           print(f"Temos um total de {vagas_disponiveis} vagas disponíveis.")
           horario_chegada= float(input("Informe seu horário de chegada:\n"))
           print("Imprimindo Ticket...")
           time.sleep(3)
           print(f"Ticket: XXX-XXX-XXX\nHora de entrada:{horario_chegada}")
           print("ATENÇÃO! Caso o Ticket for perdido ou não tiver registro no sistema, irá ser cobrado uma taxa fixa de R$50,00.")
           vagas_disponiveis = vagas_disponiveis -1

        elif vagas_disponiveis == 0:
           print("O estacionamento está lotado e sem vagas disponíveis, aguarde até que uma seja liberada\nAgradecemos a colaboração.")

      else:
         print("Opção Inválida.")


   elif escolha_menu == 2:
      escolha_saida = str(input("Informe a maneira que deseja sair:\n1- Tag\n2- Ticket\n"))

      if escolha_saida == "1":
        verificacao_tag = float(input("Insira o ID da Tag:\n"))
        horario_saida = float(input("Informe o horário de saída:\n"))

        if horario_chegada is not None:
         tempo_de_permanencia = horario_saida - horario_chegada
        print(f"Você permaneceu {tempo_de_permanencia:.2f} horas com seu veículo estacionado.")

        if tempo_de_permanencia <=0.15:
          tolerância = 0
          print("Tempo de permanência dentro da taxa gratuita.")

        elif 0.15 < tempo_de_permanencia <=3:
           valor_fixo = 15.00
        
           print(f"Valor total: R${valor_fixo}")
      
        elif tempo_de_permanencia >3:
          valor_fixo = 15.00
          hora_adicional = tempo_de_permanencia * 3 
          subtracao_de_juros = hora_adicional - 9
          
          soma_valores = valor_fixo + subtracao_de_juros
          valor_total = soma_valores - (soma_valores * 10 /100 )

        if tempo_de_permanencia > 0.15:
          if 0.15 < tempo_de_permanencia <=3:
            valor_total = 15.00
          # for >3, already set
          print(f"Valor total: R${valor_total}")
          forma_pagamento = int(input("Sua forma de pagamento:\n1-Débito\n2-Pix\n"))

          if forma_pagamento == 1:
            saldo = float(input("Digite o saldo do seu cartão:\n"))
            if saldo < valor_total:
              print("Saldo Insuficiente.")
            elif saldo >= valor_total:
              saldo_restante = saldo - valor_total
              print("Processando Transação...")
              print(f"Saldo restante R${saldo_restante:.2f}")
              print("Passagem Liberada.")
              print("Agrademos pela preferência. Volte sempre!")
              print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
              str(input("Deixe seu Feedback!\n"))
              print("Agradecemos seu Feedback!")
              
          elif forma_pagamento == 2:
            saldo = float(input("Digite o saldo em sua conta:\n"))
            if saldo < valor_total:
              print("Saldo Insuficiente.")
            elif saldo >= valor_total:
              saldo_restante = saldo - valor_total
              print("Processando Transação...")
              print(f"Saldo restante R${saldo_restante:.2f}")
              print("Passagem Liberada.")
              print("Agrademos pela preferência. Volte sempre!")
              print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
              str(input("Deixe seu Feedback!\n"))
              print("Agradecemos seu Feedback!")
          else:
            print("Selecione uma das duas formas de pagamento.\nDúvidas consultar o porteiro.")

      elif escolha_saida == "2": 
       verificacao_ticket = str(input("Você possui seu ticket?")).strip().lower()
       if verificacao_ticket == "sim":
        insercao_ticket = float(input("Insira seu Ticket:\n"))
        horario_saida = float(input("Informe o horário de saída:\n"))

        if horario_chegada is not None:
         tempo_de_permanencia = horario_saida - horario_chegada
        print(f"Você permaneceu {tempo_de_permanencia:.2f} horas com seu veículo estacionado.")

        if tempo_de_permanencia <=0.15:
           tolerância = 0
           print("Tempo de permanência dentro da taxa gratuita.")
           print("Passagem Liberada.")
           print("Agrademos pela preferência. Volte sempre!")
           print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
           str(input("Deixe seu Feedback!\n"))
           print("Agradecemos seu Feedback!")

           vagas_disponiveis = vagas_disponiveis +1

        elif 0.15 < tempo_de_permanencia <=3:
           valor_fixo = 15.00
      
        elif tempo_de_permanencia >3:
          valor_fixo = 15.00
          hora_adicional = tempo_de_permanencia * 3 
          subtracao_de_juros = hora_adicional - 9
          valor_total = valor_fixo + subtracao_de_juros

        if tempo_de_permanencia > 0.15:
          if 0.15 < tempo_de_permanencia <=3:
            valor_total = 15.00
          # for >3, already set
          print(f"Valor total: R${valor_total}")
          forma_pagamento = int(input("Sua forma de pagamento:\n1-Débito\n2-Pix\n"))

          if forma_pagamento == 1:
            saldo = float(input("Digite o saldo do seu cartão:\n"))
            if saldo < valor_total:
              print("Saldo Insuficiente.")
            elif saldo >= valor_total:
              saldo_restante = saldo - valor_total
              print("Processando Transação...")
              print(f"Saldo restante R${saldo_restante:.2f}")
              print("Passagem Liberada.")
              print("Agrademos pela preferência. Volte sempre!")
              print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
              str(input("Deixe seu Feedback!\n"))
              print("Agradecemos seu Feedback!")
              vagas_disponiveis +=1
          elif forma_pagamento == 2:
            saldo = float(input("Digite o saldo em sua conta:\n"))
            if saldo < valor_total:
              print("Saldo Insuficiente.")
            elif saldo >= valor_total:
              saldo_restante = saldo - valor_total
              print("Processando Transação...")
              print(f"Saldo restante R${saldo_restante:.2f}")
              print("Passagem Liberada.")
              print("Agrademos pela preferência. Volte sempre!")
              print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
              str(input("Deixe seu Feedback!\n"))
              print("Agradecemos seu Feedback!")
              vagas_disponiveis +=1
          else:
            print("Selecione uma das duas formas de pagamento.\nDúvidas consultar o porteiro.")

       elif verificacao_ticket == "não" or verificacao_ticket == "nao":
         print("Você deve pagar uma taxa de R$ 50,00 pela perca do ticket\nDúvidas consultar o porteiro.")
         horario_saida = float(input("Informe o horário de saída:\n"))

         if horario_chegada is not None:
           tempo_de_permanencia = horario_saida - horario_chegada
           print(f"Você permaneceu {tempo_de_permanencia:.2f} horas com seu veículo estacionado.")

         if tempo_de_permanencia <=0.15:
           valor_total = 50
           print(f"Valor total: R${valor_total}")


         elif 0.15 < tempo_de_permanencia <=3:
           valor_total = 65
           print(f"Valor total: R${valor_total}")
      
         elif tempo_de_permanencia >3:
          valor_fixo = 15.00
          hora_adicional = tempo_de_permanencia * 3 
          subtracao_de_juros = hora_adicional - 9
          valor_total = valor_fixo + subtracao_de_juros +50

         print(f"Valor total: R${valor_total}")
       forma_pagamento = int(input("Sua forma de pagamento:\n1-Débito\n2-Pix\n"))

      if forma_pagamento == 1:
         saldo = float(input("Digite o saldo do seu cartão:\n"))
         if saldo < valor_total:
            print("Saldo Insuficiente.") #===========================

         elif saldo >= valor_total:
           saldo_restante = saldo - valor_total
           print("Processando Transação...")
           print(f"Saldo restante R${saldo_restante:.2f}")
           print("Passagem Liberada.")
           print("Agrademos pela preferência. Volte sempre!")
           print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
           str(input("Deixe seu Feedback!\n"))
           print("Agradecemos seu Feedback!")

           vagas_disponiveis = vagas_disponiveis +1

      elif forma_pagamento == 2:
         saldo = float(input("Digite o saldo em sua conta:\n"))
        
         if saldo < valor_total:
          print("Saldo Insuficiente.")

         elif saldo >= valor_total:
          saldo_restante = saldo - valor_total
          print("Processando Transação...")
          print(f"Saldo restante R${saldo_restante:.2f}")
          print("Passagem Liberada.")
          print("Agrademos pela preferência. Volte sempre!")
          print("Avaliação\n1⭐\n2⭐⭐\n3⭐⭐⭐\n4⭐⭐⭐⭐\n5⭐⭐⭐⭐⭐")
          str(input("Deixe seu Feedback!\n"))
          print("Agradecemos seu Feedback!")

          vagas_disponiveis = vagas_disponiveis +1
        
       
   else:  
    print("Selecione uma opção válida.")

