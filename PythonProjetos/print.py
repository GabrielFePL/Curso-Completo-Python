# Sintaxe: print(objetos, argumentos)
mensagem = 'Função print()'
print(mensagem)
print('Aula de Python')

# Agumentos Posicionais
nome = 'Gabriel'
curso = 'Curso de Python'
print(curso, '-', nome)

# Concatenando Strings
nome = input('Digite seu nome:')
msg = 'Olá ' + nome + '! Bem-vindo ao curso.'
print(msg)

# Desabilitar quebra de linha no print
print('Esta é a linha 1 com quebra')
print('Esta é a linha 2 sem quebra, ', end='')
print('esta é a continuação da linha 2.')

# String com .format()
nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos.'.format(nome, idade)
print(msg_formatada)

# fString ou formated String
nome = 'Gabriel'
peso = 70
msg = f'Olá {nome}, seu peso é {peso}Kg.'
print(msg)

peso2 = 15
pesoAtual = f'O seu peso antigo era {peso}Kg, você ganhou {peso2}Kg e agora pesa {peso + peso2}Kg.'
print(pesoAtual)

# Formatando Casas Decimais em Strings
peso = 70.36172
print(f'O peso é {peso:.2f}')

# Inserir Caracteres de Escape
print(f'O peso é \'{peso:.2f}\'')
print(f'Nome: {nome}\tIdade: {idade}')
print(f'O caminho do arquivo é \\Arquivo.py')
print(f'O caminho do arquivo é \\\\Arquivo.py')