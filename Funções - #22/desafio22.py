def calculadora(A, B, opcao):
    def soma():
        return A + B
    def subtracao():
        return A - B
    def multiplicacao():
        return A * B
    def divisao():
        if A == 0 or B == 0:
            print("[ERRO] Divisão por zero.")
        else:
            A / B

    if opcao == 1:
        return soma()
    elif opcao == 2:
        return subtracao()
    elif opcao == 3:
        return multiplicacao()
    elif opcao == 4:
        return divisao()

while True:
    menu = """
    ====================
            MENU        
    ====================
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [0] Sair
    ====================
    """
    escolha = int(input("Escolha uma opção: "))

    if escolha == 0:
        print("Saindo da calculadora...")
        break

    if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        res = calculadora(n1, n2, escolha)
        print(f"\nO resultado é: {res}")

        escolha2 = int(input("\nDeseja retornar? Se sim, digite 1. Se não, digite 0: "))

        if escolha2 == 0:
            print("Saindo da calculadora...")
            break
        elif escolha2 == 1:
            print("Voltando...")
            continue
        else:
            print("[INVÁLIDO] Retornando por padrão.")

    else:
        print("Opção inválida! Tente novamente.")
        
