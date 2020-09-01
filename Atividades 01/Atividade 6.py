print("Especificação   |Código |Preço |")
print("Cachorro quente |100    |1,20  |")
print("Bauru simples   |101    |1,30  |")
print("Bauru com ovo   |102    |1,50  |")
print("Hambúrguer      |103    |1,20  |")
print("Cheeseburguer   |104    |1,30  |")
print("Refrigerante    |105    |1,00  |")

x = int(input("Digite o código do produto: "))
y = int(input("Digite a quantidade: "))
if x == 100:
    z = y*1.2
if x == 101:
    z = y*1.3
if x == 102:
    z = y*1.5
if x == 103:
    z = y*1.2
if x == 104:
    z = y*1.3
if x == 105:
    z = y*1
print("O valor total do pedido é de R$", z)