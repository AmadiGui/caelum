from flask import Flask, render_template, request
from web.conta import Conta
import csv


app  = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/cria_conta", methods=['POST'])
def cria():
    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    conta = Conta(numero, titular, saldo, limite)

    arquivo = open('contas.txt', 'a')
    arquivo.write(f'{conta.numero},{conta.titular},{conta.saldo},{conta.limite}\n')
    arquivo.close()

    return redirect(url_for('lista_contas'))

 #   return  'conta adicionada com suceso'
@app.route('/contas')
def lista_contas():
    arquivo = open('contas.txt','r')
    leitor_csv = csv.reader(arquivo)

    lista_contas = []

    for coluna in leitor_csv:
        conta = Conta(coluna[0], coluna[1], float(coluna[2]), float(coluna[3]))
        contas.append(conta)

    arquivo.close()

    return render_template('lista.html', contas = lista_contas)
if __name__ == '__main__':
    app.run()