import math
import os

x = 16
raiz_quad = math.sqrt(x)

print("Raiz quadrada de", x, "é igual a", raiz_quad)

angulo = 45
seno = math.sin(math.radians(angulo))
print("O seno de", angulo, "é igual a", seno)

diretorio = os.getcwd()
print(f"Diretório corrente é", diretorio)

# os.system("cls") limpa tela windows - os.system("clear") linux

lista = [10, 20, 30]
tam = len(lista)
print("A lista", lista, "tem tamanho", tam)

soma = sum(lista)
print("A lista", lista, " tem um somatório igual a", soma)