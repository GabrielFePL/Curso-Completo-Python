lista = [2, 6, 9, 4, 0, 12]
palavra = 'Gabriel'

for item in lista:
    print(item)

for letra in palavra:
    print(letra)

# Range range(valor_inicial, valor_final, incremento)
for numero in range(1, 11):
    print(numero)

for numero in range(11):
    print(numero)

palavra = input('Digite seu nome: ')
for x in range(10):
    print(f'{x + 1} {palavra}')

for x in range(2, 21, 2):
    print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira')
for pedra in pedras:
    if (pedra == 'Quartzo'):
        continue
    print(pedra)