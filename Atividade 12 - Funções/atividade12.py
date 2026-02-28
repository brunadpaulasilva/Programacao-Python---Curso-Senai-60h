#Exercícios com funções:
#variáveis locais, globais e parâmetros

#1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
def comparar_par_impar():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if n1 % 2 == 0:
        print(f"{n1} é PAR")
    else:
        print(f"{n1} é ÍMPAR")

    if n2 % 2 == 0:
        print(f"{n2} é PAR")
    else:
        print(f"{n2} é ÍMPAR")

comparar_par_impar()        

#2 - CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    n3 = int(input('Digite um numero: '))
    print(n1 * n2 * n3)

multiplicar()    

# #3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def calcular_potencia():
    numero = int(input("Digite um número: "))
    expoente = int(input("Digite o expoente: "))
    resultado = numero ** expoente
    print("Resultado:", resultado)

calcular_potencia()    

# #4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.
# def mensagem_personalizada():
#        nome = input('Digite seu nome e sobrenome: ')
#        idade = int(input('Digite sua idade: '))
#        if idade == 18:   
#             print("Seja Bem Vindo ao nosso sistema de motoristas")
#        else :
#             print("Por favor verificar idade") 

# mensagem_personalizada()
## versão melhorada do mesmo codigo:
def mensagem_personalizada():
    nome = input("Digite seu nome e sobrenome: ").strip()

    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida. Por favor, digite um número.")
        return

    if idade >= 18:
        print(f"Seja bem-vindo(a), {nome}! Você pode se cadastrar como motorista.")
    else:
        print(f"{nome}, você ainda não tem idade suficiente para se cadastrar como motorista.")

mensagem_personalizada()

# #5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def descobrir_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print("Sua idade é:", idade)

descobrir_idade()    

# #6 - DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

def jogos_copa():
    anos = ["1994", "1999", "2002"]
    consulta_jogos = input('Digite um ano: ')
    
    if consulta_jogos in anos:
        print('Neste ano o Brasil foi campeão!')
    else:
        print('Neste ano não houve jogos da copa')

jogos_copa()

#7 - DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
#1 - Função - cumprimentar o cliente
#2 - Função - restaurante
#3 - Sugestão utilize listas e loops 

def sistema_de_restaurante():

    clientes = []
    cardapio = ["Salamarão", "Macarrarão", "Sanduimarão", "Sorvemarão"]
    precos = [100.0, 150.0, 250.0, 50.0]

    print('''Sejam bem-vindos ao Restaurante Camarões!!!
Escolha o ID do cardápio:
0 - Salamarão
1 - Macarrarão
2 - Sanduimarão
3 - Sorvemarão
''')

    nome = input('Nome do cliente: ')
    clientes.append(nome)

    id_escolhido = int(input('Escolha o ID do cardápio: '))
    quantidade = int(input('Quantidade: '))

    item_escolhido = cardapio[id_escolhido]
    valor_unitario = precos[id_escolhido]

    total = valor_unitario * quantidade

    print("\n*********** NOTA ***********")
    print(f"Cliente: {nome}")
    print(f"Item: {item_escolhido}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor unitário: R$ {valor_unitario}")
    print(f"Total a pagar: R$ {total}")
    print("****************************")


sistema_de_restaurante()