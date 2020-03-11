
class Conta:

    identificador = 0

    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    

    def __init__(self, numero, titular, saldo, limite=1000.00):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta.identificador += 1

    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True


    def extrato(self):
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')
#        print(f'saldo: {self.saldo}')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True