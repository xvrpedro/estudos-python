lista = []
i = 1

while i != 0:
    elemento = int(input("Insira um número (digite 0 para parar): "))

    # adiciona na lista se for diferente de 0
    if elemento != 0:
        lista.append(elemento)
    else:
        print("Parando...")
        break

'''
comando para ver até quantos elementos tem na lista: len(<lista>)
maior: max(<lista>)
menor: min(<lista>)
'''

print(f"Quantidade de elementos: {len(lista)}; Maior: {max(lista)}; Menor: {min(lista)}.")
