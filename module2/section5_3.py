import os


os.system('cls')


# Identificar anagrama
print('=' * 80)
print('Identificador de anagrama:'.center(80))
print('-' * 80)

str_1 = input("Digite a primeira string: ")
str_2 = input("Digite a segunda string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("Não são anagramas")

print('=' * 80)
print()