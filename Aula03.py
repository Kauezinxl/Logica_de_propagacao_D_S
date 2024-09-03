nome = 'Kaue'
idade = 18

peso = input('Digite seu peso: ')

num1 = input('Digite o primeiro numero: ')
num1 = int(num1)

num2 = int(input('Digite o segundo numero: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2 
div_inteira = num1 // num2
expo = num1 ** num2
modulo = num1 % num2

# Atribuição
num1 += 1
num1 -= 1
num1 /= 1
num1 *= 1

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {div}')
print(f'Divisão Arredondada: {div:.2f}')
print(f'Divisão Inteira: {div_inteira}')
print(f'Exponenciação: {expo}')
print(f'Resto da divisão: {modulo}')
print()
print(f'O número digitado +1 é: {num1}')