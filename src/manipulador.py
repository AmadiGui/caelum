class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total

if __name__ == '__main__':
    from conta import ContaCorrente, SeguroDeVida, TributavelMixIn

    cc1 = ContaCorrente('123-4', 'Joao', 1000.00)
    cc2 = ContaCorrente('123-5', 'Jose', 1000.00)
    seguro1 = SeguroDeVida(100.0, 'Jose', '345-77')
    seguro2 = SeguroDeVida(100.0, 'Maria', '237-98')

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)