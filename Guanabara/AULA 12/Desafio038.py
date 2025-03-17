#Desafio038
#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#o segundo valor é maior
#não existe valor maior, os dois são iguais

valor1 = int(input('Digite um numero inteiro '))
valor2 =int(input('Digite o segundo numero inteiro '))

if valor1 > valor2:
  print('O Primeiro valor é maior ')
elif valor2 > valor1:
  print('O Segundo valor é maior ')
else:
  print(' Não existe valor maior, os dois são iguais ')