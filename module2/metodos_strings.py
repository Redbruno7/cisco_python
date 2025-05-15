import os


os.system('cls')


# Método capitalize() - Torna maiúsculo o primeiro caractere
print('=' * 80)
print('Método capitalize() - Exemplos:'.center(80))
print('-' * 80)

print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

print('=' * 80)
print()

# Método center() - Centraliza a string dentro do estipulado
print('=' * 80)
print('Método center() - Exemplos:'.center(80))
print('-' * 80)

print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

print('=' * 80)
print()

# Método endswith() - Verifica se a string fornecida termina com argumento especificado
print('=' * 80)
print('Método endswith() - Exemplos:'.center(80))
print('-' * 80)

if "epsilon".endswith("on"):
    print('"Epsilon" termina com "on"')
else:
    print('"Epsilon" não termina com "on"')
print()

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

print('=' * 80)
print()

# Método find() - Procura uma substring e retorna o índice da primeira ocorrência
# Valor de substring não existente: -1
# Apenas com strings
print('=' * 80)
print('Método find() - Exemplos:'.center(80))
print('-' * 80)

print("Eta".find("ta"))
print("Eta".find("mma"))
print()

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print()

# Procurar ocorrência específica
print('kappa'.find('a', 2))
print()

# Procurar todas as ocorrências
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
print()

# Procura pela primeira ocorrência, com exclusão do índice especificado
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

print('=' * 80)
print()

# Método isalnum() - Verifica se a string contém apenas dígitos ou letras
print('=' * 80)
print('Método isalnum() - Exemplos:'.center(80))
print('-' * 80)

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print()

t = 'Six lambdas'
print(t.isalnum())
print()

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())
print()

t = '20E1'
print(t.isalnum())

print('=' * 80)
print()

# Método isalpha() - Verifica se a string contém apenas letras
print('=' * 80)
print('Método isalpha() - Exemplos:'.center(80))
print('-' * 80)

print("Moooo".isalpha())
print('Mu40'.isalpha())

print('=' * 80)
print()

# Método isdigit() - Verifica se a string contém apenas dígitos
print('=' * 80)
print('Método isdigit() - Exemplos:'.center(80))
print('-' * 80)

print('2018'.isdigit())
print("Year2019".isdigit())

print('=' * 80)
print()

# Método islower() - Verifica se a string possui apenas letras minúsculas
print('=' * 80)
print('Método islower() - Exemplos:'.center(80))
print('-' * 80)

print("Moooo".islower())
print('moooo'.islower())

print('=' * 80)
print()

# Método isupper() - Verifica se a string possui apenas letras maiúsculas
print('=' * 80)
print('Método issuper() - Exemplos:'.center(80))
print('-' * 80)

print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

print('=' * 80)
print()

# Método isspace() - Verifica se a string possui apenas espaços em branco
print('=' * 80)
print('Método isspace() - Exemplos:'.center(80))
print('-' * 80)

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

print('=' * 80)
print()

# Método join() - Executa junção de string
# Elementos de uma lista unidos em uma string com separador
print('=' * 80)
print('Método join() - Exemplos:'.center(80))
print('-' * 80)

print(",".join(["omicron", "pi", "rho"]))

print('=' * 80)
print()

# Método lower() - Retorna uma cópia da string com letras minúsculas
print('=' * 80)
print('Método lower() - Exemplos:'.center(80))
print('-' * 80)

print("SiGmA=60".lower())

print('=' * 80)
print()

# Método lstrip() - Retorna uma cópia da string sem os espaços em branco iniciais ou com parâmetro
print('=' * 80)
print('Método lstrip() - Exemplos:'.center(80))
print('-' * 80)

print("[" + " tau ".lstrip() + "]")
print()

print("www.cisco.com".lstrip("w."))
print()

print("pythoninstitute.org".lstrip(".org"))

print('=' * 80)
print()

# Método replace() - Retorna uma cópia da string com os valores do primeiro argumento substituidos pelo segundo argumento
print('=' * 80)
print('Método replace() - Exemplos:'.center(80))
print('-' * 80)

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print()

# Limitar o número de substituições
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
    
print('=' * 80)
print()

# Método rfind() - Mesmo que find(), mas a partir do lado direito
print('=' * 80)
print('Método rfind() - Exemplos:'.center(80))
print('-' * 80)

print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

print('=' * 80)
print()

# Método rstrip() - Mesmo que lstrip(), mas a partir do lado direito
print('=' * 80)
print('Método rstrip() - Exemplos:'.center(80))
print('-' * 80)

print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

print('=' * 80)
print()

# Método split() - Divide a string e cria uma lista com as substrings
print('=' * 80)
print('Método split() - Exemplos:'.center(80))
print('-' * 80)

print("phi       chi\npsi".split())

print('=' * 80)
print()

# Método startswith() - Verifica se a string começa com parâmentro especificado
print('=' * 80)
print('Método startswith() - Exemplos:'.center(80))
print('-' * 80)

print("omega".startswith("meg"))
print("omega".startswith("om"))

print('=' * 80)
print()

# Método strip() - Remove todos os espaços em branco da string
print('=' * 80)
print('Método strip() - Exemplos:'.center(80))
print('-' * 80)

print("[" + "   aleph   ".strip() + "]")

print('=' * 80)
print()

# Método swapcase() - Inverte as letras maiúsculas por minúsculas e vice-versa
print('=' * 80)
print('Método swapcase() - Exemplos:'.center(80))
print('-' * 80)

print("I know that I know nothing.".swapcase())

print('=' * 80)
print()

# Método title() - Transforma em maiúsculo a primeira letra de cada palavra
print('=' * 80)
print('Método title() - Exemplos:'.center(80))
print('-' * 80)

print("I know that I know nothing. Part 1.".title())

print('=' * 80)
print()

# Método upper() - Retorna uma cópia da string com letras maiúsculas
print('=' * 80)
print('Método upper() - Exemplos:'.center(80))
print('-' * 80)

print("I know that I know nothing. Part 2.".upper())

print('=' * 80)
print()