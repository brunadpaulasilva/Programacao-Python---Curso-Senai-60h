# Atividades para trabalhar com try and except
import statistics
#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def numero():

    try:
        numero = int(input('Digite um número: '))
        print(numero)
    
    except ValueError:
        print('O número precisa ser inteiro')    

numero()

#Exercício 2:
#Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

def divisão():

    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1/n2)

    except ZeroDivisionError as error:
      print(error)

divisão()     

#Exercício 3:
#Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

def divisao():
    try:
     lista = [0,1,2,3,4,5]
     moda  =  statistics.mode(lista)
     print(moda)
    except ZeroDivisionError as erro:
        print(erro)
    except TypeError:
        print('Provavelmente digitaram letras')
    except ValueError as erro :
        print(erro)
    except NameError as erro:
        print(erro)    
    except SyntaxError as erro:
        print(erro)     
    finally:
        print('Carregamento finalizado')


divisao()  