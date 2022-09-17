"""
Variáveis podem conter número no nome, mas devem iniciar com letras
letra maiúscula se diferencia de minúscula exemplo: "variavel1" "Variavel2"
não é possível definir espaços no nome da variável, para isso use
o separador "_"
"""
# Definindo variáveis

nome = 'Matheus'  # str
idade = 19  # int
altura = 1.82  # float
maioridade = idade > 18  # bool
data_1 = False  # bool explícito tem que iniciar com letr maíscula
peso = 76  # int/float depende do valor inserido

imc = (peso / (altura ** 2))  # (altura * altura) ou (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Aaltura:', altura)
print('Peso:', peso)
print('É de maior idade?', maioridade)
print('IMC:', imc)

if imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc >= 18.5:
    print('Peso normal')
else:
    print('Baixo peso')
