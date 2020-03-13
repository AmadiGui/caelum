import abc

class Conta(abc.ABC):
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
        if (self._saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def deposita(self, valor):
        if (valor < 0):
            raise ValueError("vc não pode sacar um valor negativo")
        else:
            self.saldo += valor

    def saca(self, valor):
        if (valor < 0):
            raise ValueError('Voce nao pode sacar um valor negativo')
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

    @abc.abstractmethod
    def atualiza():
        pass
#    def atualiza(self, taxa):
#        self._saldo += self._saldo * taxa

 #   def __str__(self):
 #       return  '< numero: {self.numero}\nsaldo: {self.saldo} >'
class TributavelMixIn:
    def get_valor_imposto(self):
        pass

class ContaCorrente(Conta, TributavelMixIn):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
#class AtualizadorDeContas():
#    def __init__(self, selic, saldo_total=0):
#        self._selic = selic
#        self._saldo_total = saldo_total

#    def roda(self, conta):

class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05





if __name__ == '__main__':
#   c = Conta('123-4', 'João', 100, 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.00)
    cp = ContaPoupanca('123-6', 'Maria', 1000.00)
    ci = ContaInvestimento('123-7', 'Maria', 1000.00)

#   adc = AtualizadorDeContas (0.01)

#   adc.roda(c)
#   c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    ci.atualiza(0.01)

#   print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)
    print(ci.saldo)

#   c.extrato()
#   cc.extrato()
#   cp.extrato()

