import random
# meu_modulo.py

# **1 - Crie um número aleatório de 5,10**

def atividade_1(n1,n2):
   return random.randint(n1, n2)

# **2 - Crie 3 números aleatórios**

def at2(a,b):
    n3 = [ random.randint(a,b),
     random.randint(a,b),
     random.randint(a,b)
    ]

    return n3


# **3 - Crie um número aleatório entre 10 a 30 utilize o range()**

def atividade_3(x,y):
    n1 = random.randrange(x,y)

    return n1
