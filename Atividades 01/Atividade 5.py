x = int(input("Digite a idade do nadador: "))
z = "pd"
if x < 5:
    z = "np"
if x >= 5 and x <= 7:
    y = "Infantil A"

if x >= 8 and x <= 10:
    y = "Infantil B"

if x >= 11 and x <= 13:
    y = "Juvenil A"

if x >= 14 and x <= 17:
    y = "Juvenil B"

if x >= 18:
    y = "Adulto"
if z == "pd":
    print("O nadador está na categoria", y)
else:
    print("O nadador é muito novo")