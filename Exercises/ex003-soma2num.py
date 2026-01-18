#Faça um algoritimo que some dos números com a entrada de usuário e exiba para o cliente
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
soma = int(num1 + num2)
# Aqui, a f-string .format() é utilizada para adicionar as variáveis em ordem dentro da string de exibição (print)
print('A soma do número {} e {} é {}!'.format(num1, num2, soma))
