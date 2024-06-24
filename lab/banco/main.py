menu = """

    [d] - depositar
    [s] - sacar
    [e] - extrato
    [q] - sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Insira o valor  do depósito:\n'))
        extrato += f"Depósito de valor R${deposito:.2f}\n"
        saldo += deposito

    elif opcao == 's':
        saque = float(input('Insira o valor que deseja sacar. Limite de R$500,00 por saque e somente 3 saques diários.\n'))
        if(numero_saques >= LIMITE_SAQUES):
            print('Você já fez 3 saques hoje, tente novamente amanhã')
        else:
            if(saque >= LIMITE):
                print('O valor está acima do limite, por favor tente novamente')
            else:
                if(saldo <= 0):
                    print(f'O valor do saque está acima do seu saldo, que é R${saldo:.2f}')
                else:
                    print(f'Saque de R${saque:.2f} efetuado')
                    extrato += f"Saque de valor R${saque:.2f}\n"
                    saldo -= saque

                    numero_saques += 1
                    print(f'Você fez {numero_saques} de 3')



    elif opcao == 'e':
        print("\nEXTRATO")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break

    else:
        print('Opção inválida, por favor selecione novamente a operação desejada')
