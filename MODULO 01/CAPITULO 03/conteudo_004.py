nascimento = 1986
ano_atual = 2022
idade = ano_atual - nascimento

# TypeError: can only concatenate str (not "int") to str
"""
print('Eu tenho ' + idade + ' anos')
"""

print('Eu tenho ' + str(idade) + ' anos')  # uma maneira correta

# conversão do tipo int
print(float(10))  # 10.0
print(bool(-1))  # True
print(bool(0))  # False

# conversão do tipo float
print(int(9.999))  # 9
print(bool(-0.99))  # True
print(str(-0.99))  # '-0.99'

# conversão do tipo bool
print(int(True))  # 1
print(float(False))  # 0.0
print(str(True))  # 'True'

# conversão do tipo str
print(int('-99'))  # 99
print(float('0.01'))  # 0.00001
print(bool('palavra'))  # True
print(bool(''))  # False

# conversão para None
x = 10
print('Valor:', x, '--', type(x))
# atribuição do valor None à variável x
x = None
print('Valor:', x, '--', type(x))

print(str(None))
print(bool(None))


nascimento = 1986
ano_atual = 2022

idade = ano_atual - nascimento

print(f'Eu tenho {idade} anos')
print(f'Eu tenho {ano_atual - nascimento} anos')

palavra = 'consolação'
print(f'A palavra {palavra.upper()} possuí {len(palavra)} letras')

orcamento = 5000
vlr_gasto = 430

pct = (vlr_gasto/orcamento) * 100
print(f"Porcetagem já gasta do orçamento {pct:*>10}%")
print(f"Porcetagem já gasta do orçamento {pct:*>10.2f}%")
pct = (vlr_gasto/orcamento)
print(f"Porcetagem já gasta do orçamento {pct:*^11.2%}")
