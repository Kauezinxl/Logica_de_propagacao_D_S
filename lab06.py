lista = []

nome1 = input('Digite um nome: ')
lista.append(nome1)

nome2 = input('Digite um nome: ')
lista.append(nome2)

lista.sort()

if nome1 in lista and nome2 in lista:
    print(f'Sim, o {nome1} e o {nome2} está adicionado a lista')
else:
    print(f'Não, o {nome1} e o {nome2} não está na lista')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

if num1 > num2:
    print('é maior')
else:
    print('é menor')
    if num1 > num2:
        print('é menor')
    else:
        print('é maior')
print('fim do bloco if else')

