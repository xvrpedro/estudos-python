# FEITO COM AJUDA DA INTELIGENCIA ARTIFICIAL, 
# EXPLICANDO OS COMANDOS PARA ESTUDAR MELHOR

import operacoes

while True:
    print('''
    --- Menu ---
    1. Cadastrar Clientes
    2. Buscar por CPF
    3. Alterar Telefone
    4. Apagar Cliente
    5. Mostrar Todos
    6. Sair
    ''')
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        operacoes.cadastrar()
    elif opcao == "2":
        operacoes.buscar()
    elif opcao == "3":
        operacoes.alterar()
    elif opcao == "4":
        operacoes.apagar()
    elif opcao == "5":
        operacoes.mostrar_todos()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
