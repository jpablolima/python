""" arquivo=open('numeros.txt', 'w')
for linha in range(1,101):
    arquivo.write('%d\n' % linha)
arquivo.close()    """     

""" arquivo=open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()     """

# Impressão dos parametros passados na linha de comando
""" 
import sys
print("números de parâmetros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print('Parámetros %d = %s' % (n,p))
 """


# Geração de arquivos
#Gravação em arquivos diferentes


impares=open('impares.txt','w')
pares=open('pares.txt','w')
for n in range(0,1000):
    if n % 2 == 0:
        pares.write('%d\n' % n)
    else:
        impares.write('%d\n' % n)
impares.close()
pares.close()            