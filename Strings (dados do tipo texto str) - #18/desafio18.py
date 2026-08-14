i = ""
nome = ""

while i != "/exit":
    txt = input("Digite um nome ou /exit: ")

    if txt != "/exit":
        nome += txt + " "
    else:
        i = "/exit"

print(f"Resultado da concatenação: {nome}")