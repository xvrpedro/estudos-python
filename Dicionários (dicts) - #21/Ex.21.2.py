lista = []

for _ in range(3):
    info = {}
    info["nome"] = input("Insira seu nome: ")
    info["peso"] = float(input("Insira seu peso: "))
    info["idade"] = int(input("Insira sua idade: "))
    lista.append(info)

print("Dados das pessoas:")
for info in lista:
    print(f"Nome: {info["nome"]}")
    print(f"Peso: {info["peso"]}")
    print(f"Idade: {info["idade"]}\n")
    