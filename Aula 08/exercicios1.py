## EXERCÍCIOS 1: 
## Utilize condicionais

## Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input('Digite um número'))
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')        

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('Digite sua idade'))
if idade >= 16:
    print('Apresenta idade ideal para votar')
else: 
    print('Não apresenta idade ideal para votar')

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
variavel = int(input('Digite um número de 1 a 10: '))
if variavel == 2 or variavel == 4 or variavel == 6 or variavel == 8 or variavel == 10:
    print('Par')
else:
    print('ímpar')    

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))
if numero1 == numero2 == numero3 == numero1:
    print('Equilatero')
elif numero1 != numero2 != numero3 != numero1:
    print('Escaleno')    
else:
    print('Isósceles')   


# 5*

	# Determine se um número é múltiplo de 5 e 7.
n1 = int(input('Digite um número: '))

if n1 % 5 == 0 and n1 % 7 == 0:
    print('Múltiplo') 
else:
    print('Não é múltiplo')      

# 6*

# Verifique se um número é positivo e maior que 10
numero20 = int(input('Dígite um número: '))
if numero20 >= 10:
    print('Positivo')
elif numero20 <= -1:
    print('Negativo')    
else:
    print('É positivo e está abaixo de 10') 

# 7*

# Verifique se um número é divisível por 3 ou 5.
n3 = int(input('Digite um número: '))

if n3 % 3 == 0 and n3 % 5 == 0:
    print('Divisível') 
else:
    print('Não é Divisível')  