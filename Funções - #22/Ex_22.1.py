def maior(A, B):
    if A > B:
        return A
    else:
        return B

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

res = maior(n1, n2)

print(f"O maior número é: {res}")