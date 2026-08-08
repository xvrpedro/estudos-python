import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print("Olá seja bem-vindo(a)")

print(f'O valor inteiro em decimal é: {10: d}')
print(f'O valor inteiro em binário é: {10: b}')

print(f'O valor de pi é: {3.14159265: f}')
print(f'O valor de pi é: {3.14159265: .2f}')

# desafio
nome = "Pedro Xavier"
idade = 15
salario = 12000100.978654321
nacionalidade = "Brasileiro"
salariobr = locale.format_string("%.2f", salario, grouping=True)

print(f'Meu nome é {nome},\n Tenho {idade} anos de idade,\n Já recebo R${salario: .2f}\n E sou {nacionalidade.lower()}.')
print(f'Meu nome é {nome},\n Tenho {idade} anos de idade,\n Já recebo R${salariobr}\n E sou {nacionalidade.lower()}.')