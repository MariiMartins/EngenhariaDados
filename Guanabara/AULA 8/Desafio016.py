#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Resolução Guanabara
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

#Resolução 2 Guanabara
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))