# -*- coding: utf-8 -*-
LARGURA = 79
entrada=open('entrada.txt')
for linha in entrada.readline():
    if linha[0]==';':
        continue
    elif linha[0]=='>':
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=='*':
        print(linha[1:].center(LARGURA))
    else:
        print(linha)
entrada.close()            