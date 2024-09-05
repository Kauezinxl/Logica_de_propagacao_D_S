from time import sleep
import os

x = int(input('Digite o numero de segundos da contagem regressiva: '))

for i in range(x, -1, -1):
    print(i)
    print(1)
    os.system('cls')

~int('Fim da contagem')