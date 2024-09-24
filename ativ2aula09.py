alunos = []

while True:
    print("\n--- Boletim ---")
    print("1. Cadastrar alunos")
    print("2. Listar alunos")
    print("3. Sair")

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        nome_aluno = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        media = (nota1 + nota2 + nota3) / 3
        print(f'Nome: {nome_aluno}, Média: {media:.2f}')
        alunos[nome_aluno] = {'nome' : nome_aluno, 'media' : media}

        

    elif opcao == '2':
        visu = input('Digite o nome do aluno que deseja ver a nota: ')
        if visu in alunos:
            print(alunos[visu])
        else:
            print('Aluno não encontrado')

    elif opcao == '3': 
        print('Saindo do Sistema!')
        break

    else:
        print('Digite uma opcao válida!')