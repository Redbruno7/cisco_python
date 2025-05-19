import os


os.system('cls')


# Identificar palíndromo
print('=' * 80)
print('Identificador de palíndromo:'.center(80))
print('-' * 80)

text = input("Digite o texto: ")

# Remover todos os espaços
text = text.replace(' ','')

# Verificar se a palavra é igual à sua versão inversa
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("É palíndromo")
else:
	print("Não é palíndromo")

print('=' * 80)
print()