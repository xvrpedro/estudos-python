import json
from banco_dados import carregar_dados, salvar_dados

# 1. CADASTRO
def cadastrar():
    lista = []
    while True:
        print("\n--- Cadastro de Cliente ---")
        cliente = {
            "nome": input("Nome: "),
            "cpf": input("CPF: "),
            "telefone": input("Telefone: "),
        }
        lista.append(cliente)

        continuar = input("Deseja continuar? (s/n)")
        if continuar.lower() != 's':
            break   

    with open("clientes.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4)

# 2. BUSCA CPF
def buscar():
    dados = carregar_dados()
    cpf_busca = input("\nDigite o CPF para buscar: ")
    for i in dados:
        if i["cpf"] == cpf_busca:
            print(f"Encontrado! Nome: {i['nome']}")

# 3. ALTERAR DADOS
def alterar():
    dados = carregar_dados()
    cpf_alterar = input("\nDigite o CPF para alterar telefone: ")
    for i in dados:
        if i["cpf"] == cpf_alterar:
            i["telefone"] = input("Digite o novo telefone: ")

    salvar_dados(dados)

# 4. APAGAR
def apagar():
    dados = carregar_dados()
    cpf_apagar = input("\nDigite o CPF do cliente para apagar: ")
    for i in dados:
        if i["cpf"] == cpf_apagar:
            dados.remove(i)
            break

    salvar_dados(dados)

# 5. MOSTRAR TODOS
def mostrar_todos():
    print("\n--- Todos os Clientes Salvos no Arquivo")
    with open("clientes.json", "r") as arquivo:
        print(arquivo.read())
