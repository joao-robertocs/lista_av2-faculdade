print('Digite um número e direi se é positivo ou negativo!')
print('P = Positivo e N = negativo')
numero = int(input("Digite o número: "))

def valor(numero):
    if numero > 0:
        print(f'O {numero} é P!')
    elif numero <= 0:
        print(f'O {numero} é N!')

valor(numero)

