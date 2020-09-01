x = int(input("Digite a temperatura: "))
y = str(input("Digite c para Celsius e f para Fahrenheit: "))

if y == "c":
    print("A temperatura em Celsius é de", x, "Cº, e em Fahrenheit é de", (9/5)*x+32, "Fº")
if y == "f":
    print("A temperatura em Celsius é de", (5/9)*(x-32), "Cº, e em Fahrenheit é de", x, "Fº")