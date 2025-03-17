#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alinos e mostre a ordem sorteada
#Resolução Guanabara
import random
n1 = str(input('Nome do Primeiro aluno: '))
n2 = str(input('Nome do Segundo aluno: '))
n3 = str(input('Nome do Terceiro aluno: '))
n4 = str(input('Nome do Quarto aluno: '))
lista =[n1, n2, n3, n4]
random.shuffle(lista)
print ('A ordem de apresentação será ')
print (lista)