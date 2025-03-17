#Reescreva o programa que pergunta o salário de um funcionário e calcule seu valor de aumento.
#Para salarios superiores a R$1250 calcule um aumento de 10%
#Para os inferiores ou iguais o aumento é de 15%
s = int(input('Digite seu salario '))
if s<=1250:
  print ('Seu novo salario é R$ {:.2f}'.format(s+(s*.15)))  
else:
  print('Seu salario é {:.2f}'.format(s+(s*.1)))

#Resolução Guanabara  
salario = float(input('Qual é o salario do funcionário? R$ '))
if salario <=1250:
  novo = salario + (salario*15/100)
else:
  novo = salario + (salario*10/100)  
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))  