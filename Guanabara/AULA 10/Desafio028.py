#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O Programa deverá escrever na tela se o usuário venceu ou perdeu
import random
n = int(input('Digite um numero entre 0 e 5 \n '))
p = random.randint(0, 5)
if n == p:
	print("Você Venceu!")
else:
	print("Você perdeu!")

#Resolução Guanabara
from random import randint
computador = randint(0,5)
print('-=-'*10)
print('Vou pensaem em um numeto entre 0 e 5. Tente adivinhar....')
print('-=-'*10)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
  print('PARABÉNS VOCÊ CONSEGUIU ME VENCER')
else:
  print('GANHEI! Eu pensei no numero {} e não no {}'. format(computador, jogador))  