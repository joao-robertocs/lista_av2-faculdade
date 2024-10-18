def soma(num1,num2):
    resultado_soma = num1 + num2
    return resultado_soma

def subtrair(num1,num2):
    resultado_subtrai = num1 - num2
    return resultado_subtrai

def multiplica(num1,num2):
    resultado_multiplica = num1 * num2
    return resultado_multiplica

def divide(num1,num2):
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

    if escolha == '1':
        resultado = soma(num1,num2)
        print(resultado)
    elif escolha == '2':
        resultado = subtrair(num1,num2)
        print(resultado)
    elif escolha == '3':
        resultado = multiplica(num1,num2)
        print(resultado)
    elif escolha == '4':
        resultado = divide(num1,num2)
        print(resultado)