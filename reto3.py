numero_reg = int(input())
carros = []
nope = True
for i in range(numero_reg):
    carro = input().split()
    carros.append(carro)
for i in range(numero_reg):
    for x in range(len(carro)):
        carros[i][x] = int(carros[i][x])
for i in range(numero_reg):
    cumple = 0
    if carros[i][0] >= 1200 and carros[i][0] < 3600:
        cumple += 1
    if carros[i][1] > 2018:
        cumple += 1
    if carros[i][2] <= 30000:
        cumple += 1
    if carros[i][3] < 35:
        cumple += 1
    if carros[i][4] < 26000:
        cumple += 1
    if cumple == 5:
        nope = False
        print(carros[i][4]-12000)
if nope:
    print("NO DISPONIBLE")