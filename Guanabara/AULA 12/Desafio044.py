#Desafio044
#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
#a vista dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#em aé 2x no cartão: preço normal
#3x ou mais: 20% de juros

valor = float(input('Valor do Produto:'))
print('1 - A Vista: dinheiro ou cheque\n 2 -A vista no cartão \n 3 - 2x no cartão\n 4 - 3x ou mais no cartão')
pagamento = str(input('Qual condição de pagamento será? '))

if pagamento == 1: 
  c1 = valor - (valor*0.1)
  print(c1)
elif pagamento == 2: 
  c2 = valor - (valor*0.05)
  print(c2)
elif pagamento == 3: 
  c3 = valor
  print(c3)  
else:
  c4 = valor + (valor*.2)
  print(c4)  


#Resolução Guanabara
print('{:=^40}'.format (' LOJAS GUANABARA '))
preco = float(input('Preço das Compras: R$'))
print(''' Qual será o modo de PAGAMENTO:
1 - A Vista: dinheiro/ cheque
2 - A vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
opcao = int(input('Qual condição de pagamento será? '))
if opcao == 1: 
  total = preco - (preco*0.1)
elif opcao == 2: 
  total = preco - (preco*0.05)
elif opcao == 3: 
  total = preco
  parcela = total /2
  print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
  total = preco + (preco*.2)
  totparc = int(input('Quantas parcelas? '))
  parcela = total / totparc
  print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:  
  total =0
  print('OPÇÃO INVALIDA DE PAGAMENTO')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
