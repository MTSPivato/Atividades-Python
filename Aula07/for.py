"""
For in em Python
Inteando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra =='h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# for n in range (0, 100, 9):
#     print(n)
