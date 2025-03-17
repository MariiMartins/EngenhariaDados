#Desafio 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros
n1 = float(input('Digita o tamanho ae: \n'))
c = n1*100
m = n1*1000
print('Seu valor é {:.0f} cm , e em milimetros é {:.0f} mm'. format(c,m))