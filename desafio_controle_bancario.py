menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
total_deposito = 0
total_saque = 0
total_erros = 0
while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            total_deposito +=1
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            total_erros +=1
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            total_erros +=1
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            total_erros +=1
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            total_erros +=1
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            total_saque +=1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            total_erros +=1
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        print(f"\nTotal de Depositos: {total_deposito}")
        print(f"\nTotal de Saques   : {total_saque}")
        print(f"\nTotal de Erros    : {total_erros}")
    elif opcao == "9":
        print("Agradecemos a preferência!!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")