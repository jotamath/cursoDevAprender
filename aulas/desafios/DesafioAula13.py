# DESAFIOS 🎖️

#DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
count = 1
while count <= 120:
    print(count)
    count += 1

#DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = ''
while senha != 'secreto':
    senha = input('Digite a senha: ')

#DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1
count = 100
while count >= 1:
    print(count)
    count -= 1
