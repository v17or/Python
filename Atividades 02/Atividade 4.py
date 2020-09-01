cont = 0
par = 0
impar = 0
maior = 0

for cont in range (20):
    num=int(input("Digite um numero: "))
    if (num % 2 == 0):
        par += num
    else:
        impar += num
print("Soma dos pares: {} \nSoma dos Ímpares: {}".format(par, impar)) 