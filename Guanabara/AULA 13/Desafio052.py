#Desafio052
#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num +1):
  if num % c ==0:
    print('\033[34m')
    tot +=1
  else:  
    print('\033[m')
print('\n O número {} foi dividido {}x '.format(num, tot))
if tot ==2:
  print('É PRIMO')
else:
  print ('NÃO É PRIMO')