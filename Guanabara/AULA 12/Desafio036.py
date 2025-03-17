#Desafio036
#Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

casa = float (input('Qual o valor da casa? '))
salario= float (input('Qual seu salário? '))
tempo = float (input('Em quanto tempo em anos pretende pagar? '))

valor = salario*0.3
meses = tempo*12
prestacao = casa/meses

print('O valor de {}, e com o salario de {} pretendendo pagar em {} anos, a prestação será de {:.2f}'.format(casa,salario, tempo, prestacao))

if prestacao >= valor:
  print('Emprestimo negado')
else:
    print('Sua prestação é de {:.2f}'.format(prestacao))