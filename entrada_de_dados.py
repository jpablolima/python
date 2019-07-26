""" nome = input('Digite seu nome: ')
num = input('Digite um número: ')
print (nome, num)

print('você digitou %s' %nome)
print("olá, %s" %nome)

 """

# Conversão de Dados de Entrada

""" anos = int(input('Anos de serviço: '))
valor_por_ano = float(input('valor por ano: '))
bonus= anos * valor_por_ano
print('bonus  de R$ %5.2f' %bonus) """

# soma de valores inteiros

""" print('Soma de Valore inteiros!')
num_int1 = int(input('Digite um valor inteiro: '))
num_int2 = int(input('Digite um segundo valor inteiro: '))
soma = num_int1 + num_int2
print('Total:', soma)
 """
# Conversão de Metros em Milimetros

""" print('Conversão de Metros em Milimertros! Com números Inteiros')

metros = int(input('Digite um em metros:'))
milimetros = (metros)  * 1000
print(milimetros, 'mm') """


# Calculo de Segundos

dias = int(input('Digite o número de dias: ')) 
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos=int(input('Digite os segundos:')) 

total_dias_segundos = (dias) * 86400
total_horas = (horas) * 3600
total_minutos = (minutos) * 60
total_segundos = (segundos) * 1
print(total_dias_segundos,'em segundos')
print(total_horas,'em segundoss')
print(total_minutos,'em segundos')
print(total_segundos,'em segundos')
total = (total_dias_segundos + total_horas + total_minutos + total_segundos)
print('total em segundos:', total)


