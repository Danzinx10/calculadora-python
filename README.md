# Autor: Daniel de Macêdo
# Data de criação: 2025-05-09

while True:
    print('Olá mundo! Me diga dois números e eu te direi o calculo deles!')
    try:
        num1 = float(input('Digite o primeiro número: '))
    except ValueError:
        print('Valor inválido! Por favor, digite um número.')
        continue
    try:
        num2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Valor inválido! Por favor, digite um número.')
        continue

# Exibe as opções de operações
    try:
        print('Agora me diga qual operação você quer fazer:')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        op = int(input('Digite o número da operação: '))
    except ValueError:
        print('Valor inválido! Por favor, digite um número.')
        continue    
# Realiza a operação escolhida

    if op == 1:
        print(f'A soma de {num1} + {num2} é igual a {num1 + num2}')
    elif op == 2:
        print(f'A subtração de {num1} - {num2} é igual a {num1 - num2}')
    elif op == 3:
        print(f'A multiplicação de {num1} * {num2} é igual a {num1 * num2}')
    elif op == 4:
        if num2 == 0:
            print('Não é possível dividir por zero!')
        else:
            print(f'A divisão de {num1} / {num2} é igual a {num1 / num2}')
    else:
        print('Operação inválida! Tente novamente.')
    print('Obrigado por usar o meu programa!')
    print('Até logo!')


    continuar = input('Você quer fazer outra operação? (s/n): ')
    if continuar.lower() != 's':
        print('Saindo do programa...')
        import time
        time.sleep(2)
        print('Até logo!')
        import sys
        sys.exit()
        break

# Fim do código
