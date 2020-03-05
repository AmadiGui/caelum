import jogo_adivinha
import forca

print('\n***********************')
print('*        MENU           *')
print('***********************\n')
print("1. Adivinhacao")
print("2. Forca")
escolha = int(input("Qual jogo quer jogar. Digite um numero:"))

if escolha == 1:
    #jogar adivinhacao
    jogo_adivinha.jogar()
elif escolha == 2:
    #jogar forca
    forca.jogar()

