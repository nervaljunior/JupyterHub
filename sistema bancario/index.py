from flask import Flask, render_template, request

app = Flask(__name__)

saldo = 0
limite = 500
extrato_str = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato_str
    if valor > 0:
        saldo += valor
        extrato_str += f"Depósito: R$ {valor:.2f}\n"
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."
    else:
        return "Operação falhou! O valor informado é inválido."

def sacar(valor):
    global saldo, extrato_str, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif valor > 0:
        saldo -= valor
        extrato_str += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return f"Saque de R$ {valor:.2f} realizado com sucesso."
    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."
    else:
        return "Operação falhou! O valor informado é inválido."

def transferir(valor, destino):
    global saldo, extrato_str, limite, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif excedeu_limite:
        return "Operação falhou! O valor da transferência excede o limite."
    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."
    elif valor <= 0:
        return "Operação falhou! O valor informado é inválido."
    else:
        saldo -= valor
        extrato_str += f"Transferência para conta {destino}: R$ {valor:.2f}\n"
        numero_saques += 1
        return f"Transferência de R$ {valor:.2f} para a conta {destino} realizada com sucesso."

@app.route("/", methods=["GET", "POST"])
def home():
    global saldo, limite, extrato_str, numero_saques

    if request.method == "POST":
        opcao = request.form.get("opcao")

        if opcao == "d":
            valor = float(request.form.get("valor"))
            mensagem = depositar(valor)

        elif opcao == "s":
            valor = float(request.form.get("valor"))
            mensagem = sacar(valor)

        elif opcao == "t":
            valor = float(request.form.get("valor"))
            conta_destino = request.form.get("conta_destino")
            mensagem = transferir(valor, conta_destino)

    return render_template("index.html", saldo=saldo, limite=limite, extrato=extrato_str, numero_saques=numero_saques, mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
