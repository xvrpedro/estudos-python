lista = []

# para cada linha (são 3 colunas)
for j in range(3):
    linha = []
    # para cada coluna (4 colunas)
    for i in range(4):
        elemento = int(input("Insira o valor: "))
        linha.append(elemento)
    lista.append(linha)

maior = max(max(linha) for linha in lista)
menor = min(min(linha) for linha in lista)

print(f"Maior número: {maior}; Menor número: {menor}.")