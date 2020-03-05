
def velocidade_media(distancia, tempo):
    #velocidade = distancia/tempo
    velocidade = divisao(distancia, tempo)
    return velocidade

print(velocidade_media(100, 20))

def soma_dois_numeros(valor1, valor2):
    soma = valor1 + valor2
    return soma
print(soma_dois_numeros(2, 2))

def subtrai_dois_numeros(valor1, valor2):
    diferenca = valor1 - valor2
    return diferenca
print(subtrai_dois_numeros(2, 2))

def calculadora(valor1, valor2):
    return valor1 + valor2, valor1 - valor2, valor1 * valor2, valor1 // valor2
print(calculadora(2, 2))

def divisao(valor1, valor2):
    return valor1 / valor2
