# Simples, Composto e Encadeado
n1 = n2 = 0
media = 0

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!')
print('Sua média é {}'.format(media))

if (media >= 7):
    print('Resultado: Aprovado!')
else:
    print('Aluno reprovado...')

if (media >= 7):
    print('Resultado: Aprovado!')
elif (media >= 5):
    print('Você está de recuperação.')
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))