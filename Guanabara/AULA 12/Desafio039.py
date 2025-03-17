#Desafio039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
#se ja passou do tempo do alistamento.
#seu programa também deverá mostrar o tempo que falta ou que já passou do prazo

ano = int(input('Que ano você nasceu? '))

conta = 2021 - ano

if conta < 18:
	f = 18 - conta
	print('Sua hora de se alistar vai chegar, faltam {} anos'.format(f))
elif conta == 18:
	print('SUA HORA CHEGOU')
else:
	p = conta - 18
	print('Já passou {} anos do tempo de alistamento'.format(p))

#Resolução Guanabara
from datetime import date
atual=  date.today().year
nasc = int(input('Que ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
	print('SUA HORA CHEGOU')
elif idade < 18:
  saldo = 18 - idade
  print('Ainda faltam {} anos para o alistamento'.format(saldo))
  ano= atual + saldo
  print ('Seu alistamento será em {} '.format(ano))
elif idade > 18:
  saldo = idade -18
  print('Você já deveria ter se alistado. Passaram-se {} anos'.format(saldo))
  ano = atual - saldo
  print('Seu alistamento foi em {}'.format(ano))