## Declaração de variáveis
saldo = float(1000)
numero_saques = 1
LIMITE_SAQUE = 3
extrato = ''

## Declaração de Funções


## Menu Interativo
menu = '''

Bem-Vindo ao seu Banco, qual opção deseja?
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair

'''

while True:

    opcao = input(menu)

    if opcao == '1':
        print('Você escolheu a opção SACAR')
        valor_sacar = float(input('Quanto deseja sacar? '))
        if valor_sacar <= 500 and saldo >= valor_sacar and valor_sacar >= 0 and LIMITE_SAQUE >= numero_saques:
            numero_saques += 1
            print(f'Você está sacando R${valor_sacar}')
            saldo -= valor_sacar
            print(f'Seu saldo atual é R${saldo}')
            extrato += (f'Saque feito no valor de R${valor_sacar} \n')

        else:
            print('Parece que você não pode fazer este tipo de saque!')    

    elif opcao == '2':
        print('Você escolheu a opção DEPOSITAR')
        valor_deposito = float(input('Quanto você deseja depositar? '))
        if valor_deposito >= 0:
            print(f'Você está depositando R${valor_deposito}')
            saldo += float(valor_deposito)
            print('Seu saldo atual é R$',saldo)
            extrato += (f'Depósito feito no valor de R${valor_deposito} \n')
        else:
            print('Você não pode fazer esse tipo de depósito')

    elif opcao == '3':
        print('Você escolheu a opção EXTRATO')
        print(extrato)
        print(f'Seu saldo atual é R${saldo}')

    elif opcao == '0':
        print('Você escolheu a opção SAIR')
        break

    elif opcao == '8':
        print(numero_saques)

    else:
        print('Parece que houve um erro, tente novamente!')