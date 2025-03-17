#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
ano = int(input('Digite um ano: '))
if ano%4 == 0:
  print('é bissexto')
else:
  print ('não é bissexto')  

#Resolução Guanabara  
from datetime import date
ano = int(input('Que ano quer analisar? \n Coloque 0 para analisar o ano atual: \n'))
if ano ==0:
  ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('é bissexto')
else:
	print('não é bissexto')
