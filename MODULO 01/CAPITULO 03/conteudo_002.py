x, y = 7, 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x**y)

print(type(10 + 5))
print(type(10 + 3.5))

print(10 + False)  # Equivale a 10 + 0
print(True + 5)  # Equivale a 1 + 5
print(True + True + False)  # Equivale a 1 + 1 + 0


# maior que
x > y


# menor que
x < y


# maior igual que
x >= y


# menor igual que
x <= y


# igual que
x == y


# diferente
x != y


# exemplos
x = 5
y = 1
s = 'palavra'
print('x > y:', x > (y + 2))
print('x <= 5.564:', x <= (4.564 + 1))
print('s == palavra:', s == 'palavra')
print('(y * 0) == False:', (y * 0) == False)
print('s != abacaxi:', s != 'abacaxi')


# verifica se uma pessoa pode dirigir
idade = 23
possui_cnh = False
print(idade > 18 and possui_cnh)

# verifica se um passageiro pode viajar sozinho
idade = 15
possui_autorizacao = True
print(idade > 18 or possui_autorizacao)


print(True or False)
print((10 > 1) and True)
print(not (True or False))
print(not ('palavra' == 'palavra'))
