# -*- coding: utf-8 -*-
import time

""" agora=time.time()
print(agora)

time.ctime(agora)
print(agora)

agora2=time.localtime()
print(agora2) """

agora=time.localtime()
print("Ano: %d" % agora.tm_year)
print("Mes: %d" % agora.tm_mon)
print("Dia: %d" % agora.tm_mday)
print("Hora: %d" % agora.tm_hour)
print("Minuto: %d" % agora.tm_min)
print("Segundo: %d" % agora.tm_sec)
print("Dia da Semana: %d" % agora.tm_wday)
print("Dia no Ano: %d" % agora.tm_yday)
print("Horario de Verao: %d" % agora.tm_isdst)