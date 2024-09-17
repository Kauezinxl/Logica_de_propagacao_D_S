import os
lista_usuario = []

while True:

    print()
    print(30*'*', 'Menu', 30*'*')
    print('1. Cadastrar usuario.')
    print('2. Listar usuario.')
    print('3. Excluir usuario.')
    print('4. Buscar pelo nome.')
    print('5. Ingerir posição.')
    print('6. Sair')
    print(30*'*', 'Menu', 30*'*')

    opcao = input('Digite a opcao desejada: ')

    # Cadastrar usuario
    if opcao == '1':
        nome = input('Digite o nome que deseja cadastrar: ').upper

        if nome != '':
            lista_usuario.append(nome)
        else:
            print('Digite algum valor!')
    
    #listar usuario
    elif opcao == '2':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}° {n}')

    #Excluir usuario
    elif opcao == '3':
        for i, n in enumerate(lista_usuario):
            print(f'{i}: {n}')

        posição = int(input('Digite o numero do usuario que deseja excluir: '))

        for j, in enumerate(lista_usuario):
            if j == posição:
                lista_usuario.pop(j)
                print(f'Usuario da posição {j} foi removido!')

        '''
        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print('Usuario removido com sucesso')
        '''

    # Buscar pelo usuario
    elif opcao == '4':
        nome_buscar = input('Digite o nome que deseja buscar na lista: ').upper()

        if nome_buscar != '':
            for i in lista_usuario:
                if i == nome_buscar:
                    print(i)

    # inserir em uma posição
    elif opcao == '5':
        novo_nome = input('Digite o nome que deseja inserir: ').upper()
        posição_nome = int(input('Digite a posicao que deseja inserir: '))

        posição_nome -=1
        if posição_nome >= 0 and posição_nome <= len(lista_usuario):
            lista_usuario.insert(posição_nome, novo_nome)
        else:
    
    #Sair
    elif opcao == '6':
        print('Saindo do sistema!')
        break
 