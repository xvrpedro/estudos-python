nome = input("Digite seu nome: ")
sobrenome = input("Informe seu último nome: ")

comp_nome = len(nome)
comp_sobrenome = len(sobrenome)

nome_completo = nome + " " + sobrenome

comp_nome_completo = len(nome_completo)

print(
    f"{nome} tem: {comp_nome} letras.\n"
    f"{sobrenome} tem: {comp_sobrenome} letras.\n"
    f"Nome completo: {nome_completo}. \n"
    f"Tudo tem: {comp_nome_completo} letras. ({nome} + {sobrenome})"
)