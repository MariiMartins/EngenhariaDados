#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR
n = int(input('Digite um numero: '))
if n%2 == 0:
  print('é par')
else:
  print ('é impar')  

#Resolução Guanabara  
numero = int(input('Me diga um número qualquer: '))
resultado = numero%2
if resultado ==0:
  print('O número {} é PAR'.format(numero))
else:
  print('O número {} é IMPAR'.format(numero))