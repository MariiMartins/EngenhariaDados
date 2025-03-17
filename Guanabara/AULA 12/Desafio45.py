#Desafio045
#Crie um programa que faça o computador jogar jokenpô com você

from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções são
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='* 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='* 12)
if computador == 0:
  if jogador ==0:
    print('EMPATE')
  elif jogador ==  1:
    print('JOGADOR VENCE')
  elif jogador == 2:  
    print('COMPUTADOR VENCE')
  else:
    print('OPÇÃO INVALIDA')  
elif computador ==1:
  if jogador ==0:
    print('COMPUTADOR VENCE')
  elif jogador ==  1:
    print('EMPATE')
  elif jogador == 2:  
    print('JOGADOR VENCE')
  else:
    print('OPÇÃO INVALIDA')   
elif computador ==2:  
  if jogador ==0:
    print('JOGADOR VENCE')
  elif jogador ==  1:
    print('COMPUTADOR VENCE')
  elif jogador == 2:  
    print('EMPATE')
  else:
    print('OPÇÃO INVALIDA')
   