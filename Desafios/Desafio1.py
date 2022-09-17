"""
* Criar variável para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa
* Obter o ano de nascimento da pessoa (baseado em sua idade aual)
* Obter IMC com 2 casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
# Obs: O ano tem um "." para inticar a porcentagem daquele ano/idade, no caso eu fracionei o mês usando regra de 3
# assim ficando:
# 1° Mês = 8,33
# 2° Mês = 16,67
# 3° Mês = 25,00
# 4° Mês = 33,33
# 5° Mês = 41,67
# 6° Mês = 50,00
# 7° Mês = 58,33
# 8° Mês = 66,67
# 9° Mês = 75,00
# 10° Mês = 83,33
# 11° Mês = 91,67
# 12° Mês = 100,00

# Exemplo 19.91 = 19 anos e 11 meses ou 2022.75 = Setembro de 2022


nome = 'Matheus'
idade = 19.91
altura = 1.81
peso = 76.4
ano = 2022.75 - idade
imc = peso / (idade ** 2)

if imc > 30:
    imcr = 'obeso'
elif imc >= 25:
    imcr = 'com sobrepeso'
elif imc >= 18.5:
    imcr = 'com um peso normal'
else:
    imcr = 'abaixo peso'

print('{} nasceu em {:.2f}, logo ele tem {} anos, mede {}, pesa {}, seu IMC é de {:.2f}, logo ele está {}'.format(nome, ano, idade, altura, peso, imc, imcr))
