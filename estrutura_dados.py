lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maiorValor = lista[0]
menorValor = lista[0]
paresValor = lista[0]

for index in range(0, len(lista)):
    if(maiorValor < lista[index]):
       maiorValor = lista[index]
print(maiorValor)

for index in range(0, len(lista)):
    if (menorValor > lista[index]):
        menorValor = lista[index]
print(menorValor)

for index in lista:
    if index % 2  == 0:
        paresValor = index
        print(index, end = " ")

