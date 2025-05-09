print('Olá mundo! Me diga dois números e eu te direi o calculo deles!')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('Agora me diga qual operação você quer fazer:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
op = int(input('Digite o número da operação: '))

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
# Fim do código
