#Desafio 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
n1 = float(input('Digita o quanto você tem em R$: \n'))
d = float((n1/3.27))
print('Você pode comprar U$ {:.2f} '.format(d))