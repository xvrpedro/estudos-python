dados = {
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}

print("Dados da pessoa: ")
print("Nome:", dados["nome"])
print("Peso:", dados["peso"])
print("Idade:", dados["idade"])

dados["nome"] = "Texto"
dados["peso"] = 99.99
dados["idade"] = 10

print("Dados da pessoa: ")
print("Nome:", dados["nome"])
print("Peso:", dados["peso"])
print("Idade:", dados["idade"])

dados["nome"] = input("Insira seu nome: ")
dados["peso"] = float(input("Insira seu peso: "))
dados["idade"] = int(input("Insira sua idade: "))

print("Dados da pessoa: ")
print("Nome:", dados["nome"])
print("Peso:", dados["peso"])
print("Idade:", dados["idade"])
