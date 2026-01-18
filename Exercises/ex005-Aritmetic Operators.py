#Operadores Aritiméticos
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
soma = int(num1) + int(num2)
subt = int(num1) - int(num2)
mult = int(num1) * int(num2)
div = int(num1) / int(num2)
pot = int(num1) ** int(num2)
divint = int(num1) // int(num2)
rest = int(num1) % int(num2)
print ('Soma: {}, Subtração {}, Multiplicação {}, Divisão {},'
       'Potenciação: {}, Divisão Inteira: {}, Resto {}'
       .format(soma, subt, mult, div, pot, divint, rest))