## EXERCÍCIOS com match/ case:

## 2: Verificando se um número é positivo, negativo ou zero
numero = int(input('numero: '))

match numero:
    case 0:
        print ("Zero")
    case x if x > 0:
        print ("Positivo")
    case x if x < 0:
        print ("Negativo")

## 3: Verificando se uma string é vazia ou não
texto = input('Digite algo: ')

match texto:
    case '':
        print ('vazia')
    case _:
        print ('preenchido')    

## 4: Verificando se um número é maior, menor ou igual a 10
numero = int(input('numero: '))

match numero:
    case 10:
        print ("Igual")
    case x if x > 10:
        print ("Maior")
    case x if x < 10:
        print ("Menor")

## 5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)
idade = int(input('Idade: '))

match idade:
    case 12:
        print ("criança")
    case x if x <= 17:
        print ("adolescente")
    case x if x <= 35:
        print ("jovem")
    case x if x >= 35:
        print ("adulto")
    case x if x <= 64:
        print ("adulto")        
    case x if x > 65:
        print ("idoso")