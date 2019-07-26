""" a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
if a > b:
        print('primeiro valor maior: ',a)
if b > a:
        print('segundo valor maior:',b) """

""" idade = int(input('idade do carro:'))
if idade <= 3:
    print('carro novo!')
if idade > 3:
    print('carro velho!')             """

# Valor da multa

""" velocidade =  int(input('Digite a velocodade: '))
exesso = velocidade - 80
multa = exesso * 5

if velocidade > 80:
    print('Multa por exesso de velocidade', 'Multa de R$', multa) 
if velocidade <= 80:
    print('Dentro da velocidade permitida!')


 """

# Calculo de Imposto de Renda

""" salario = float(input('Digite o valor do Salário para calculo do imposto:'))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print('Salário: R$%6.2f Imposto a pagar: R$%6.2f' % (salario, imposto))         """

# Maior e menor valor 
""" 
num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
num3 = int(input('Digite o terceiro valor:'))

if num1 > num2 > num3:
    print('maior valor:',num1, 'menor valor:', num3)
if num2 > num1 > num3:
    print('maior valor:',num2,'menor valor:', num3)
if num3 > num1 > num2:
    print('maior valor:',num3, 'menor valor:', num2)   
if num2 > num1 > num2:
    print('maior valor:',num3, 'menor valor:', num2)      
      

     """
# If e Else

""" idade = int(input('Digite a a idade do carro: '))
if idade <= 2:
    print('carro novo!', idade,'anos')
else :
    print('carro velho!', idade, 'anos')    """ 

# Preço da Distância 

""" distancia = float(input('Informe a distância desejada: '))
distancia1= 0.50
distancia2 = 0.45

if distancia <=200:  
    valor = distancia * 0.50
    print('Valor da passagem: R$%5.2f' %valor)
else :
    valor = distancia * 0.45
    print('Valor da passagem: R$%5.2f' %valor)    
 """


 # Preço de  Conta Telefonica
""" minutos = int(input('Digite quantos minutos você utilizou: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else: 
        preco = 0.15

print('Você vai pagar este mês: R$%6.2f' %(minutos * preco))
 """

# Elif
""" categoria = int(input('digite a categoria do produto: '))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
   preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('Categiria invalida, digite um valor entr 1 e 5!')
    preco =  0
print(' preço do produto: R$%6.2f' % preco)    """             

""" num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if operacao == 1:
    soma = +
elif operacao == 2:
    subtracao = -
elif operacao == 3:
    multiplicacao = *
elif operacao == 4:
    divisao = /
else:
    print(num1 + num2)'resultado'))                 """
    