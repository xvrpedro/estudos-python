import json

# Carrega os dados pura e diretamente
def carregar_dados():
    with open("clientes.json", "r") as arquivo:
        return json.load(arquivo)

# Salva os dados pura e diretamente
def salvar_dados(dados):
    with open("clientes.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
