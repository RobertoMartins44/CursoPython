#Funções

def hello (meu_nome):
  print ('Olá',meu_nome)

hello('Roberto')

def hello1 (meu_name,idade):
  print('Olá',meu_name, ', Sua Idade é: ',idade)

hello1('Roberto',44)

def calcular_pagamento (qtd_horas,valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas < 40:
    salario = horas * taxa
  else:
    h_excd = horas - 40
    salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario

str_horas = input ('Digite as horas: ')
str_taxa  = input ('Digite a taxa: ')
total_salario = calcular_pagamento (str_horas,str_taxa)
print ('O valor de seus rendimentos é R$ :',total_salario)







#lambda função anonima
x = 5
y = 8
soma = lambda x,y: x + y
print(soma)

#import pandas as pd
#from geopy import geocode
#from math import pi, sqrt

#def calc_area (point1,point2):
#  x1,y1 = point1
#  x2,y2 = point2
#  return (x1*y2 - y1*x2) / 2

