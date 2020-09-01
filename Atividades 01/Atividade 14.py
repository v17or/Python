x = int(input("Digite a duração da chamada em minutos: "))
if x <= 3:
    valor = 1.15
if x > 3:
    valor = 1.15 + (x-3)*0.26
print("O total a ser pago será de R$", valor)