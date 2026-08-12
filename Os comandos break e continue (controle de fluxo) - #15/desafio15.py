i = 0

while True:
    res = input(f" Contador: {i}. Digite \"s\" para incrementar ao contador ou \"n\" para parar: ")

    if (res == "s"):
        i += 1
        continue
    elif (res == "n"):
        break

    print("Número inválido")

print(f"O contador chegou ao numero: {i}")