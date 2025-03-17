#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido
#Resolução Guanabara
import random
n1 = str(input('Nome do Primeiro aluno: '))
n2 = str(input('Nome do Segundo aluno: '))
n3 = str(input('Nome do Terceiro aluno: '))
n4 = str(input('Nome do Quarto aluno: '))
lista =[n1, n2, n3, n4]
escolhido = random.choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))