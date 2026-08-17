def quadrado(lista):
    for elem in lista:
        quad = elem ** 2
        print(f"O quadrado de {elem} é: {quad}")

lista = []

while True:
    num = int(input("Digite seu número inteiro (ou 0 para parar): "))

    if num == 0:
        break
    else:
        lista.append(num)
    
res = quadrado(lista)