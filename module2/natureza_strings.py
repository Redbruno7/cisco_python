import os


os.system('cls')


# Contagem de strings
# Exemplo 1
word = 'by'
print('-' * 80)
print(len(word))
print('-' * 80)
print()

# Exemplo 2
empty = ''
print('-' * 80)
print(len(empty))
print('-' * 80)
print()

# Exemplo 3
i_am = 'I\'m'
print('-' * 80)
print(len(i_am))
print('-' * 80)
print()

# Exemplo 4
multiline = '''Line #1
Line #2'''

print('-' * 80)
print(len(multiline))
print('-' * 80)
print()
print()


# Operações em strings
str1 = 'a'
str2 = 'b'

print('-' * 80)
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
print('-' * 80)
print()

# Função ord().
char_1 = 'a'
char_2 = ' '

print('-' * 80)
print(ord(char_1))
print(ord(char_2))
print('-' * 80)
print()

# Função chr().
print('-' * 80)
print(chr(97))
print(chr(945))
print('-' * 80)
print()
print()


# Sequência de strings
# Indexar strings.
the_string = 'silly walks'

print('-' * 80)
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()
print('-' * 80)
print()

# Iterar string.
the_string = 'silly walks'

print('-' * 80)
for character in the_string:
    print(character, end=' ')
print()
print('-' * 80)
print()
print()


# Fatiamento de strings
# Fatiar
alpha = "abdefg"

print('-' * 80)
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
print('-' * 80)
print()
print()


# Operadores in / not in
alphabet = "abcdefghijklmnopqrstuvwxyz"

print('-' * 80)
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
print('-' * 80)
print()

print('-' * 80)
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)
print('-' * 80)
print()
print()


# Inserção em strings
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print('-' * 80)
print(alphabet)
print('-' * 80)
print()
print()


# Função min()
print('-' * 80)
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
print('-' * 80)
print()

t = [0, 1, 2]
print(min(t))
print('-' * 80)
print()
print()


# Função max()
print('-' * 80)
print(max("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))
print('-' * 80)
print()
print()


# Método index():
print('-' * 80)
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
print('-' * 80)
print()
print()


# Função list():
print('-' * 80)
print(list("abcabc"))
print('-' * 80)
print()
print()


# Método count():
print('-' * 80)
print("abcabc".count("b"))
print('abcabc'.count("d"))
print('-' * 80)
print()