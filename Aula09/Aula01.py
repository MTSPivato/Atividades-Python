
nome = 'Matheus'
idade = 19
altura = 1.81
peso = 76
imc = peso / (altura ** 2)

if imc > 30:
    imcr = 'obeso'
elif imc >= 25:
    imcr = 'com sobrepeso'
elif imc >= 18.5:
    imcr = 'com um peso normal'
else:
    imcr = 'abaixo peso'

# Conceito F-Strings

print(f'{nome} tem {idade} anos, mede {altura} metros, pesa {peso} e tem um imc de {imc:.2f} então ele está {imcr}')
print('{} tem {} anos, mede {} metros, pesa {} e tem um imc de {:.2f} então ele está {}'.format(nome, idade, altura, peso, imc, imcr))
print('{0} tem {1} anos, mede {2} metros, pesa {3} e tem um imc de {4:.2f} então ele está {5}'.format(nome, idade, altura, peso, imc, imcr))
print('{n} tem {i} anos, mede {a} metros, pesa {p} e tem um imc de {im:.2f} então ele está {ir}'.format(n = nome,i = idade,a = altura,p = peso,im = imc,ir = imcr))
