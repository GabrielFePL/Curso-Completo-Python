num = 1
while (num <= 10):
    print(num)
    num += 1
print('Laço encerrado')

nome = None
while True:
    nome = input('Digite seu nome ou x para parar:')
    if (nome == 'x' or nome == 'X'):
        break
    print(f'Bem-vindo {nome}')
print('Até logo!')