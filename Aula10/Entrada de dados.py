"""
Entrada de dados
"""
"""
nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
ano_nascimento = 2022 - (int(idade))

print()
print(f'{nome} nasceu em {ano_nascimento}')
"""

num_1 = input('Digite um número: ')
num_2 = input('Digite mais um número: ')
print()
print('Tipo de operações matemáticas:')
print()
print('Adição = a')
print('Multiplicação = m')
print('Divisão = d')
print('Subtração = s')
print()
tconta = input('Qual operação matemática você deseja fazer? ')
print()

if tconta == 'a':
    result = (float(num_1) + float(num_2))
    print(f'{num_1} + {num_2} = {result:.2f}')
elif tconta == 'm':
    result = (float(num_1) * float(num_2))
    print(f'{num_1} x {num_2} = {result:.2f}')
elif tconta == 'd':
    result = (float(num_1) / float(num_2))
    print(f'{num_1} / {num_2} = {result:.2f}')
elif tconta == 's':
    result = (float(num_1) - float(num_2))
    print(f'{num_1} - {num_2} = {result:.2f}')
else:
    print('Processo inválido, tente novamente')
