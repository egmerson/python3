nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome: ')
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome ao total tem {} Letras'.format(len(nome)-nome.count(' ')))
nome1 = nome.split()
print('Seu primeiro nome tem {} Letras'.format(len(nome1[0])))