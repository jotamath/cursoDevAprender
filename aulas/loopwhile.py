#loop while
tentativas = 0
while tentativas < 3:
    print('tente novamente')
    tentativas += 1

#senha
nomeDeUsuario = input('Digite seu nome de Usuário: ')
senha = ''
while senha != '1234':
    senha = input('Digite a Senha: ')
print(f'Bem vindo, {nomeDeUsuario}')

#contador com while
horario = 17
while horario <= 0:
    print(horario)
    horario -= 1