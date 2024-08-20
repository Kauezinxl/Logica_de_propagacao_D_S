nome = input('Escreva seu nome: ')
email = input('Escreva seu e-mail: ')
num_tel = input('Digite seu número de telefone: ')
capacidade_total = 55
autonomia_gasolina = 14
autonomia_alcool = 12
distancia = 32
preco_gasolina = float(input('Informe o valor da gasolina: '))
preco_alcool = float(input('Informe o valor do alcool: '))
num_dia = 20
total_km = distancia*2*num_dia
l_gasolina_mes = total_km/autonomia_gasolina
l_alcool_mes = total_km/autonomia_alcool
preco_total_gasolina = l_gasolina_mes*preco_gasolina
preco_total_alcool = l_alcool_mes*preco_alcool

print(f'Seu gasto mensal de gasolina será: R$ {preco_total_gasolina:.2f}')
print(f'Seu gasto mensal de álcool será: R$ {preco_total_alcool:.2f}')
print(f'O total de kilometros que voce roda por mês é: {total_km}')