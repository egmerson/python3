nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
nome1 = int(len(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[nome1-1]))
