""" def soma(a,b):
    print(a+b)
soma(4,8)
soma(4,7)
soma(40,45) """

""" def soma(a,b):
    return(a+b)
print(soma(2,8))     """

""" def par(x):
    return(x%2 == 0)
print(par(2))
print(par(3))
print(par(10))  
print(par(11))  """

"""  def par(x):
     return(x%2==0)
def par_ou_impar(x):
    if par(x):
        return 'par'
    else:
        return 'impar'
print(par_ou_impar(4))
print(par_ou_impar(1))            

 """

## Pesquisa em um lista

""" def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
        return None
l = [10,20,25,30]
print(pesquise(l,25))
print(pesquise(l,27))   """

""" def maior(a,b):
    if a > b:
        print(a)
    else:
        print(b)
maior(5,6)
maior(1,3)
maior(7,7) """

""" 
def area (base,altura):
    return ((base  * altura)/2)
print(area(6,9))
print(area(5,8))      """



""" def soma(l):
    total=0
    for e in l:
        total+=e 
    return total
def media(l):
    return(soma(l)/len(l))    
 """

 ## Fatorial 
 
""" def fatorial(n):
    fat = 1
    while n>1:
       fat*=n 
       n-=1
    return fat     """



# Variaveis Globais e Locais

""" EMPRESA="Liga da Justiça LTDA"  
def imprime_cabecalho():
    print(EMPRESA)
    print("-" * len(EMPRESA))
 
 """

""" a = 5
def muda_e_imprime():
    a=7
    print('A dentro da função: %d' % a)
print('A antes de mudar: %d' % a)
muda_e_imprime()
print('A depois de mudar %d' % a) """

## Funções Recursivas
## Funções Recursivas Fatorial


""" 
def fatorial(n):
    print('Calculando fatorial de %d' %n)
    if n==0 or n == 1:
        print('Fatorial de %d = 1' %n)
        return 1
    else:
        fat = n*fatorial(n-1)
        print('fatorial de %d = %d' %(n, fat))
    return fat
fatorial(8)            
   """

## Validação 
""" 
while True:
    v=int(input('Digite um valor entre 0 e 10:'))
    if v <0 or v > 10:
        print( 'Valor inválido!')
    else:
        break    """

# Função Lambda
""" a = lambda x: x*2
print(a(3))         """