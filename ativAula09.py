# Dicionario de produtos

nome = input('Digite o nome do produto: ')
nome1 = input('Digite o nome do produto: ')
nome2 = input('Digite o nome do produto: ')
preco = float(input('Digite o preco do produto 1: '))
preco1 = float(input('Digite o preco do produto 2: '))
preco2 = float(input('Digite o preco do produto 3: '))
estoque = int(input('Digite a quantidade em estoque: '))
estoque1 = int(input('Digite a quantidade em estoque: '))
estoque2 = int(input('Digite a quantidade em estoque: '))

produtos = {
    101 : {f'Nome' : nome, preco : estoque },
    102 : {f'Nome' : nome1, preco1 :  estoque1 },
    103 : {f'Nome' : nome2, preco2 :  estoque2 }
}

for code, info in produtos.items():
    print(f'Código: {code}')
    print(f'nome: {info['Nome']}')
    print(f'preço: {info['preco']}')
    print(f'estoque: {info['estoque']}')
    print()