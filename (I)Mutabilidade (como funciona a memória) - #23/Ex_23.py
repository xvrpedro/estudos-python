'''
num_imutavel = 5
print(f"\nO número é: {num_imutavel}")
print("Antes")
print(f"ID: {id(num_imutavel)}")

'''
'''
como string é imutável, o python vai destruir a variável antiga 
e criar outra
com o valor novo
'''
'''

num_imutavel = 10
print(f"\nO número é: {num_imutavel}")
print(f"ID: {id(num_imutavel)}")
'''
lista_mutavel = [10, 20, 30]
print("Antes")
print(f"\nConteúdo da lista: {lista_mutavel}")
print(f"ID: {id(lista_mutavel)}")

'''
como lista é mutável, o python vai só substituir os valores
sem criar uma nova variável
'''

lista_mutavel.append(40)
lista_mutavel[0] = 0
print("\nDepois")
print(f"\nConteúdo da lista: {lista_mutavel}")
print(f"ID: {id(lista_mutavel)}")
