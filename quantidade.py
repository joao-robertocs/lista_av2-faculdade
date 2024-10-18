import math
numero = abs(int(input('Digite um número: ')))
digitos = int(math.log(numero, 10) + 1)
print(f'O {numero} tem {digitos} digitos.')