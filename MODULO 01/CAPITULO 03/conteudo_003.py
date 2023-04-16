palavra = 'consolação'

# indices positivos
print('Primeiro caractere:', palavra[0])
print('Segundo caractere:', palavra[1])
print('Sexto caractere:', palavra[5])
print('Último caractere:', palavra[9])

# indices negativos
print('Último caractere:', palavra[-1])
print('Penúltimo caractere:', palavra[-2])
print('Antepenultimo caractere:', palavra[-3])
print('Primeiro caractere:', palavra[-10])

palavra = 'consolação'
segunda_palavra = "efé"

# consola
print(palavra[:7])

# sol
print(palavra[3:6])

# sola
print(palavra[3:7])

# ação
print(palavra[6:10])

# palavra original
print(palavra[:])

# palavra[3.5] # erro
# palavra[99] # erro

s1 = 'Belo'
s2 = 'Horizonte'
# Concatenação (+)
print(s1 + s2)
print(s1 + ' ' + s2)
print(s1 + ' Monte')
# Repetição
print(s1 * 5)
print(((s1 + ', ') * 4)[:len(s1) * 4])

s1 = 'consolação'
s2 = 'sola'
print(s1 in s2)
print(s2 in s1)
print('solar' in s1)
print('solar' not in s2)

palavra = 'consolação'
print(len(palavra))

s1 = 'Belo Horizonte'
s2 = 'Esta é uma frase, com uma vírgula.'

print(s1.upper())  # todas as letras maiúsculas
print(s1.lower())  # todas as letras minúsculas
print(s2.title())  # primeira letra de cada palavra em maísculo

print(s1.replace('Horizonte', 'Monte'))  # substitui 'Horizonte' por 'Monte'

print(s1.startswith('Belo'))  # verifica se a string começa com 'Belo'
print(s1.endswith('Monte'))  # verifica se a string termina com 'Monte'

# retorna o índice da primeira ocorrência da palavra frase
print(s2.find('frase'))

print(s2.split())  # particiona a string em outras, que são separadas por um espaço
print(s2.split(','))  # particiona a string em outras, que são separadas por ','

s3 = ' palavra com espaços '
print(s3.strip())  # remove os espaços extras no início e fim da string


print('nome'.upper())
print('a, b, c, d'.split(','))
print('Belo Horizonte'.replace('Horizonte', 'Monte'))
