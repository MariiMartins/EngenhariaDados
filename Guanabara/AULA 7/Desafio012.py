#Desafio012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Digite o valor: \n'))
d = (p-(p*.05))
print ('O valor após o desconto é de {:.2f}'.format(d))

#Resolução Guanabara
preco = float(input('Digite o valor em R$: \n'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f} ,\n na promoção com 5% vai custar R$ {:.2f} '.format(preco, novo))
