x = int(input("Digite um número: "))

if x >= 0:
    y = "positivo"
else:
    y = "negativo"

if x%2 == 0:
    z = "par"
else:
    z = "ímpar"
print("O número é", z, "e é", y)
