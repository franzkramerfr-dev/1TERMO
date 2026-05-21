from machine import Pin

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)

print("Digite:")
print("1 = Ligar LED 1")
print("2 = Desligar LED 1")
print("3 = Ligar LED 2")
print("4 = Desligar LED 2")

print("sair = encerrar programa")

while True:
    comando = input ("Comando: ")
    
    if comando == "1":
        led1.on()
        print("LED 1 Ligado")
        
    elif comando == "2":
        led1.off()
        print("LED 1 Desligado")
        
    elif comando == "3":
        led2.on()
        print("LED 2 Ligado")
        
    elif comando == "4":
        led2.off()
        print("LED 2 Desligado")
        
    elif comando.lower() == "sair":
        print("Programa Encerrado")
        break
    
    else:
        print("Comando Inválido")