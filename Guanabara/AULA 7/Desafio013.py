#Desafio013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Digite o salário: \n'))
a = (s + (s * .15))
print('O valor após o aumento é de {}'.format(a))