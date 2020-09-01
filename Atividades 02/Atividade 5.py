left = 0
right = 0
balas = 5
num = 0
arvore = 0

arvore=int(input("Digite um número de 1 a 100: "))
for cont in range (100):
    num=int(input("Atire: "))
    if (num < arvore):
        print("Mais para a direita!")
        balas -= 1
    elif (num == arvore):
        print("Acertou!")
        balas -= 1
        break
    else:
        print("Mais para a esquerda!")
        balas -= 1
    print ('O número de balas é: {}' .format(balas))