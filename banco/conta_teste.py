from conta import Conta

conta = Conta('123-4', 'João', 120.0, 1000.0)
conta2 = Conta('123-5', 'Maria', 300.0 , 1000.0)

#conta.saca(20.0)
conta.transfere_para(conta2, 10.0)

conta.extrato()


