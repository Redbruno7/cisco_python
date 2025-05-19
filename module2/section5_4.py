import os


os.system('cls')


# Calcular número da vida
print('=' * 80)
print('Número da vida:'.center(80))
print('-' * 80)

date = input("Digite sua data de nascimento (no formato AAAAMMDD ou AAAAYDDMM, 8 dígitos): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Seu número de vida é: " + date)

print('=' * 80)
print()