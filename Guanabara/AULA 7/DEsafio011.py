#Desafio011
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessarua para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input('Digita a largura: \n'))
h = float(input('Digite a altura: \n'))
a = (l*h)
t = (a/2)
print ('Será necessário {} litros de tinta'.format(t))

#Resolução Guanabara
l = float(input('Digita a largura: \n'))
h = float(input('Digite a altura: \n'))
a = (l*h)
t = (a/2)
print ('Será necessário {:.2f} litros de tinta para pintar {:.2f} m²'.format(t, a))