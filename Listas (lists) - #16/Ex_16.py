lista = []

for i in range(1,6):
    elemento = int(input("Informe um elemento para lista: "))
    lista.append(elemento)

for elemento in lista:
    print(elemento, end=" ")

media = int(sum(lista)) / int(len(lista))

print(f"Média dos elementos: {media}")