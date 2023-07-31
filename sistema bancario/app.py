from flask import Flask, render_template, request

app = Flask(__name__)

def extrato(extrato_str):

    return extrato_str

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
    saldo = 0
    limite = 500
    extrato_str = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    if request.method == "POST":
        opcao = request.form.get("opcao")

        if opcao == "d":
            valor = float(request.form.get("valor"))
            if valor > 0:
                saldo += valor
                extrato_str += f"Depósito: R$ {valor:.2f}\n"

        elif opcao == "s":
            valor = float(request.form.get("valor"))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            extrato(extrato_str)
            
        elif opcao == "t":
            valor = float(request.form.get("valor"))
            conta_destino = request.form.get("conta_destino")
            transferir(valor, conta_destino)
        elif opcao == "q":
            print("aqui falta criar rota para sair")

    return render_template("index.html", saldo=saldo, limite=limite, extrato=extrato_str, numero_saques=numero_saques)

if __name__ == "__main__":
    app.run(debug=True)
