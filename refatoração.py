def calcular(num1,num2,escolha):
    if escolha == '1':
        resultado_soma = num1 + num2
        return resultado_soma
    elif escolha == '2':
        resultado_subtrai = num1 - num2
        return resultado_subtrai
    elif escolha == '3':
        resultado_multiplica = num1 * num2
        return resultado_multiplica
    elif escolha == '4':
        resultado_divide = num1 / num2
        return resultado_divide

while True:
    print('Selecione a operação:')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair')

    escolha = input('Escolha uma opção: (1/2/3/4/5) ')

    if escolha == '5':
        print('Fechando!')
        break

    num1 = float(input('Digite seu primeiro número: '))
    num2 = float(input('Digite seu segundo número: '))

    resultado = calcular(num1,num2,escolha)
    print(f'O resultado deu {resultado}')