vetor01 = []
vetor02 = []
i = 0
num = 0

for i in range (10):
    num=int(input("Digite um numero: "))
    vetor01.append(num)

i = 0
num = 0
for i in range (10):
    num=int(input("Digite um numero: "))
    vetor02.append(num)

num = vetor01 + vetor02
print (num)
