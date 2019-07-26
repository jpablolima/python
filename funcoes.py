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

empresa="Liga da Justiça LTDA"  
def imprime_cabecalho():
    print(empresa)
    print("-" * len(empresa))
 
