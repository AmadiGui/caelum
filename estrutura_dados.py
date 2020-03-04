lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maiorValor = lista[0]

for index in range(0, len(lista)):
    print(index)
    if(maiorValor < lista[index]):
        print(maiorValor, lista[index])
        maiorValor = lista[index]

#print(maiorValor)

#menorValor = lista[0]
#
#for index in range(0, len(lista)):
#    if (menorValor > lista[index]):
#        menorValor = lista[index]
#
#print(menorValor)