# Importa o namespace do módulo 'math' para o script.
import math
num = int(input('Digite um número: '))
# Exige o prefixo 'math.' para acessar a função, garantindo que não haja conflito com outras funções locais.
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz:.1f}')

# Extrai apenas a função 'sqrt', economizando memória e digitação.
from math import sqrt
num2 = int(input('Digite um número: '))
# Permite o uso direto do nome da função, tornando a sintaxe mais limpa e direta.
raiz2 = sqrt(num2)
print(f'A raiz de {num2} é {raiz2:.1f}')

# Carrega o módulo completo, exigindo o uso do prefixo para acessar funções.
import random
num3 = random.randint(1,100)
# A função randint(a, b) gera um número inteiro aleatório incluindo os limites 1 e 100.
print(f'Seu número da sorte é {num3}!')

# Importa apenas a função randint para o escopo global do script.
from random import randint
num4 = randint(1,100)
# Permite chamar a função diretamente, o que torna o código mais conciso em scripts simples.
print(f'Seu número da sorte é {num4}!')