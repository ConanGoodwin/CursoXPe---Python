limiar = 5

menores = []
maiores = []

for num in range(10):
    if num < limiar:
        menores.append(num)
    elif num > limiar:
        maiores.append(num)

print("Resulyado final")
print("maiores:", maiores)
print("menores:", menores)
