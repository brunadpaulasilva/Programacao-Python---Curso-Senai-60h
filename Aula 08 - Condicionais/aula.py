# estruturas de dados
# 4 tipos dados boleano inteiros decimais texto

## comentarios da professora:

# var 
# lista []
# tuplas ()
# conjuntos {} 
# dicionarios{key:valor}


# nome  =  'fernando'
# lista  =  [1,2,3,5, 'teste']
# print(lista[0])
# tuplas  =  (1,2,3,6)
# prin(tupla[0])
# tupla_2 = 1,2,3,6
# dicionarios = {
# 'key':'value',
# 'key2':{


# 'a':20


# }
# }


# print(dicionarios['key2']['a'])


# estruturas de fluxo de controle 


# palavra_reservada condição = v or f


nome  = input('digite seu nome: ')


# utilização do pass
# if nome == 'Fernanda':
#     pass


# condicional  simples


# falso
if nome  == 'Kaio':
    print('Seja bem vindo', nome)


# verdadeiro
if nome != 'Kaio':
    print('Não pode acessar ... ')


# condicional composta


if nome == 'kaio':
    print('seja bem vindo', nome)
else:
    print('Não pode acessar ... ')    


# condicional composta if elif else



if nome == 'Kaio':
    print('Seja bem vindo ', nome)
elif nome == 'Lucas':
    print('Não pode acessar')
elif nome == 'Fenanda':
    print('Olá', nome)    
else:
    print('faça o cadastro')




# só posso inciar condicionais com if
# elif quantos eu quiser 
# else só tem um (dentro de um fluxo de condição)
# if só tem um (dentro de um fluxo de condição)
