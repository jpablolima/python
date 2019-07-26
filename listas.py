""" z = [ 15, 8, 9 ]
z[0]  """

# Calculo de média

""" notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x +=1
print('Média: %5.1f' %(soma/x))     """

""" notas = [0,0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input('Digite as notas %d:' %x))
    soma += notas[x]
    x +=1
x = 0
while x<7:
    print('notas %d %6.1f' %(x, notas[x]))
    x +=1
print('media: %5.2f' %(soma/x))        
 """

# Apresentação de números
""" 
numeros=[0,0,0,0,0]
x = 0
while x<5:
    numeros[x]=int(input('numero %d:' %(x+1)))
    x+=1
while True:
    escolhido=int(input('Que posição você quer imprimir (0 pra sair:)'))
    if escolhido == 0:
     break
    print('você escolheu o número: %d' %(numeros[escolhido-1]))
     """
""" L = [1,2,3]
x = 0
while x < 3:
    print(L[x])
    x +=1 """
""" 
L=[]
while True:
    n = int(input( 'Digite um número (0 sai):'))
    if n == 0:
        break
        L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x= x+1         """


# Simulação de uma Fila de Banco - Pilhas
""" 
ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print('\nExiste %d clientes na fila' %len(fila))
    print('\n Fila atual:', fila)
    print( 'Digite E para adicionar novo cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operacao = input('Operacao(F, A , S):')
    if operacao == 'A':
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print('Cliente  %d atendido' % atendido)
        else:
            print('Fila Vazia ! Ninguém pra atender') 
    elif operacao == 'E':
        ultimo+=1 #incrementa ticket do novo cliente 
        fila.append(ultimo)
    elif operacao == 'S':
            break
    else:
        print('Operação invalida! Digita apenas F, A ou S')              """

# Pesquisa Sequencial
""" 
L = [15,7,27,39]
p=int(input('Digite um valor pra procurar:'))
achou=False
x = 0
while x <len(L):
    if L[x]==p:
        achou=True
        break
    x+=1
if achou:
    print('%d achado na posição %d' %(p,x))
else:
    print('%d não encontrado!' % p)         """    


 ####################
""" L = [8,9,15]
for e in L:
    print(e)     """
####################    

## Copia de elementos para outra lista

""" v = [9,8,7,12,15,0,13,21,31]
p=[]
i=[]
for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)
print('Pares:', p)
print('Impares:', i)  

 """

## Controle de Salas de Cinema

""" lugares_vagos = [10,2,1,3,0]
while True:
    sala=int(input('Sala( 0 sai):'))
    if sala == 0:
        print('Fim')
        break
    if sala>len(lugares_vagos) or sala<1:
        print('Sala invalida')
    elif lugares_vagos[sala-1]==0:
        print('Desculpe, sala lotada!')
    else:
        lugares = int(input('Quantas lugares você deseja(%d vagos):'
        % lugares_vagos[sala-1]))
        if lugares> lugares_vagos[sala-1]:
            print('Esses número de lugares não está disponivel!')
        elif lugares < 0:
            print('número inválido')
        else:
            lugares_vagos[sala-1]-=lugares
            print('%d lugares vendidos' % lugares)
print('Utilazação das salas')
for x, l in enumerate(lugares_vagos):
    print('salas %d - %d lugar(es) vazio(s)' % (x+1, 1)) """

## Listas com Strings

s = ['maças', 'peras', 'kiwis']
print(len(s))

