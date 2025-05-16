import os


os.system('cls')


# Comparação strings
# Igualdade
print('=' * 80)
print('Igualdade "==" - Exemplos:'.center(80))
print('-' * 80)

print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print()

print('alpha' == 'Alpha')
print('alpha' != 'alpha')

print('=' * 80)
print()

# Menor
print('=' * 80)
print('Menor ">" - Exemplos:'.center(80))
print('-' * 80)

print('alpha' < 'alphabet')
print('alphabet' < 'alpha')

print('=' * 80)
print()

# Maior
print('=' * 80)
print('Maior ">" - Exemplos:'.center(80))
print('-' * 80)

print('beta' > 'Beta')
print('Beta' > 'beta')

print('=' * 80)
print()

# Outros exemplos
print('=' * 80)
print('Outros Exemplos:'.center(80))
print('-' * 80)

print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
print()

print('=' * 80)
print()

# Função sorted() - Criada uma nova lista
print('=' * 80)
print('Função sorted()'.center(80))
print('-' * 80)

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print('=' * 80)
print()

# Função sort() - Não é criada nova lista
print('=' * 80)
print('Função sort()'.center(80))
print('-' * 80)

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

print('=' * 80)
print()

# Conversão de valores de string
print('=' * 80)
print('Conversão de valores'.center(80))
print('-' * 80)

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
print()

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

print('=' * 80)
print()

# Conversão de valores de string
print('=' * 80)
print('Conversão de valores'.center(80))
print('-' * 80)

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
print()

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

print('=' * 80)
print()

