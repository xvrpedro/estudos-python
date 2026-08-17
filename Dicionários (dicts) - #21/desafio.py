lista = []

for _ in range(5):
    produto = {}
    produto["id"] = int(input("Insira o id do produto: "))
    produto["preco"] = float(input("Insira o preço: "))
    produto["nome"] = input("Insira o nome: ")
    lista.append(produto)

    print(f"\nProdutos cadastrados: {len(lista)}")

    for produto in lista:
        print(f"Id: {produto["id"]}")
        print(f"Preço: {produto["preco"]}")
        print(f"Nome: {produto["nome"]}\n")

