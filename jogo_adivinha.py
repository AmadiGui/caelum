print('\n***********************')
print('* jogo da adivinhacao *')
print('***********************\n')

numero_secreto = 42
numero_tentativas = 3
rodada = 1
for rodada in range(1, numero_tentativas+1):
###while (rodada <= numero_tentativas):
    print(f"Rodada {rodada} de {numero_tentativas}")
    #recebeo chute
    chute = int(input("digite um numero: \n"))
   
    print("você digitou", chute)

    igual = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    #compara o chute com o numero secreto
    if  igual:
        print("você acertou o numero secreto.")
        break
    elif menor:
        print("você errou ! digitou um numero menor que o secreto.") 
    elif maior:
        print("você errou ! digitou um numero maior que o secreto.")

   ### rodada = rodada +1
print("Fim de Jogo")
