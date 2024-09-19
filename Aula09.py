import os
lista_produtos = []
quantidade = []
preco = []
nome_produto = []
total = []
soma = []

while True:
    print()
    print(3*'-', 'Gerenciamento de produtos', 3*'-')
    print('1. Adicionar produto.')
    print('2. Atualizar quantidade de produto.')
    print('3. Listar todos os produtos.')
    print('4. Calcular valor total do estoque.')
    print('5. Sair')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        nome_produto = input('Digite o nome do produto: ').upper()
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o preço do produto: '))
        lista_produtos.append(nome_produto)

    elif opcao == '2':
        nome_produto = input('Digite o nome do produto: ').upper()
        if nome_produto in lista_produtos:
            posicao = lista_produtos.append(nome_produto)
            quantidade = int(input('Digite a nova quantidade do produto: '))
            print('Nova quantidade atualizada!')
        else:
            print('Produto não encontrado.')

    elif opcao == '3':
        for i, n in enumerate(lista_produtos):
            if nome_produto in lista_produtos:
                print(f'{i + 1}° {n}, Quantidade: {quantidade}, e o valor: R${preco}')
            else:
                print('Nenhum produto cadastrado.')

    elif opcao == '4':
        for i, n in enumerate(lista_produtos):
            if nome_produto in lista_produtos:
                total.append(quantidade[i] * preco[i])
                soma.append(quantidade[i] * preco[i])
                print(f'Valor total do {n}: R${total[i]:.2f}')
            else:
                print('Nenhum produto cadastrado.')

    elif opcao == '5':
        print('Saindo do mercado.')
        break