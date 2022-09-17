"""
Tipos de dados

ste - string: 'Assim' "Assim"
int - inteiro: 0 10 20 30 40 -10 -20 -30 -40
float - real/ponto flutuante: 12.5 15.8 87.2 0.0 1.1 2.2
bool - booleano/lógico: True/False 10==10
"""

"""
# Tipo de dados aplicado

print('Teste', type('Teste'))
print(25, type(25))
print(25.5, type(25.5))
print(1 == 1, type(1 == 1))
print(1 == 2, type(1 == 2))
print('a' == 'a', type('a' == 'a'))
print('a' == 'A', type('a' == 'A'))
"""

"""
# bool identifica espaços vazios e 0 como false, exemplos:

print('Texto', type('Texto'), bool('Texto'))  # Irá imprimir como "True"
print('Texto', type('Texto'), bool(''))  # Irá imprimir como "False"
print(1, type(1), bool(1))  # Irá imprimir como "True"
print(0, type(0), bool(0))  # Irá imprimir como "False"
"""

"""
# É possível converter strings em número utilizando "int" ou "float"

print('32', int('32'))
print('32.23', float('32.23'))
"""

# Modelo cadastro

# Nome = string
print('Matheus', type('Matheus'))

# Idade = int
print(19, type(19))

#  Altura = float
print(1.82, type(1.82))

# Maior de idade
print(19 > 18, type(19 > 18))
