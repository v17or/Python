cont = 0
maior = 0
while (cont < 15):
    num=int(input("Digite um numero: "))
    if (num > 30):
        maior = maior + 1
    cont = cont + 1
else:

    print("No total são",maior, "maiores que 30!")