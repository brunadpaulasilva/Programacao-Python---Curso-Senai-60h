## ***ATIVIDADE 1***

## 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

contador = 1
while contador <= 1000:
     print("Número:", contador)
     contador += 1

## 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# c = 0

# while c <= 5:
#     print(c)
#     c = c + 1     

lista_nomes  = ['Maria','Bruna','Jeferson','Leandro','Melissa','Clara','Victor','Rafael','Maite','Fernando']
quantidade  =  int(input('Quantidade: '))
# for n in range(quantidade):
#         nota = float(input('Nota: '))
#         lista_notas.append(nota)
# else:
#     print('notas', lista_notas)    
#     print('media', sum(lista_notas)/len(lista_notas))    

# quantidade  =  int(input('Quantidade: '))

# mesmo código com while

while quantidade > 10:
        nome = input(('Digite um nome: '))
        lista_nomes.append(nome)
        quantidade = quantidade - 1
else:
    print('nome', lista_nomes)    