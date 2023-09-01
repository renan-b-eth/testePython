tempertura = int(input("Digite a temperatura: "))

if tempertura > 25:
    print("Quente")
elif tempertura < 18 and tempertura >=0:
    print("Frio")
else: 
    print("Abaixo de zero")
