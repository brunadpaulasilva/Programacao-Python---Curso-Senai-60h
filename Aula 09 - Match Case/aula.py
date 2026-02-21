## Match Case
numero = int(input( 'numero: '))


match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('impar') 