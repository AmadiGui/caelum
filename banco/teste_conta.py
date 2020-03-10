def cria_conta(numero, titular, saldo, limite):
    """
    cria_conta(numero, titular, saldo, limite)
    Função que cria uma conta dados os parametros:
    titular: str
    numero: str
    saldo: float
    limite: float
    """

    conta = {"numero": numero, "titular:": titular, "saldo": saldo, "limite": limite}
    return conta 

def deposita(conta, valor):
    conta['saldo'] +=valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

if __name__ == '__main__':

    conta = cria_conta('123-7', 'João', 500.0, 1000.0)

    deposita(conta, 50.00)
    saca(conta, 20)
    extrato(conta)