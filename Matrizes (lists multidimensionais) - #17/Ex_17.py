mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Penúltimo elemento da matriz:", mat[2][1])

print("Todos os elementos da primeira linha:")

for i in mat[0]:
     print(i, end=" ")

print()
print("Todos os elementos númericos da lista:")

for j in mat:
    for i in j:
        print(i, end=" ")

print("Acabou")