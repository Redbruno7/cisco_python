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

# Exercício
print('=' * 80)
print('Exercício'.center(80))
print('-' * 80)

digits = [
    '1111110',  	# 0
    '0110000',  # 1
    '1101101',  # 2
    '1111001',  # 3
    '0110011',  # 4
    '1011011',  # 5
    '1011111',  # 6
    '1110000',  # 7
    '1111111',  # 8
    '1111011',  # 9
]


def print_number(num):
    global digits
    digs = str(num)
    lines = ['' for lin in range(5)]
    for d in digs:
        segs = [[' ', ' ', ' '] for lin in range(5)]
        ptrn = digits[ord(d) - ord('0')]
        if ptrn[0] == '1':
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
        for lin in range(5):
            lines[lin] += ''.join(segs[lin]) + ' '
    for lin in lines:
        print(lin)


print_number(int(input("Enter the number you wish to display: ")))

print('=' * 80)
print()