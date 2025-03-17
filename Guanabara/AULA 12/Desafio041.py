#Desafio041
# A confedereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#9 anos MIRIM
#14 anos INFANTIL
#19 JUNIOR
#20 SENIOR
#acima MASTER

ano = int(input('Digite seu ano de nascimento '))
categoria = 2021 - ano

if categoria <=9:
  print('MIRIM')
elif categoria <=14:
  print('INFANTIL')
elif categoria <=19:
  print('JUNIOR')
elif categoria == 25:
  print('SENIOR') 
else:
  print('MASTER')   

#Resolução Guanabara
from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento '))
idade = atual - ano
if idade <=9:
  print('MIRIM')
elif idade <=14:
  print('INFANTIL')
elif idade <=19:
  print('JUNIOR')
elif idade <= 25:
  print('SENIOR') 
else:
  print('MASTER')    