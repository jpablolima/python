""" arquivo=open('numeros.txt', 'w')
for linha in range(1,101):
    arquivo.write('%d\n' % linha)
arquivo.close()    """     

""" arquivo=open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()     """

# Impressão dos parametros passados na linha de comando

import sys
print("números de parâmetros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print('Parámetros %d = %s' % (n,p))


