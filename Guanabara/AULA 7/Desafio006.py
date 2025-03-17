#Desafio 006
#Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada
n1 = int(input('Digita um numero: \n'))
d = n1*2
t= n1*3
r= n1**(1/2)
print('O dobro é {}, o triplo é {}, e a raíz quadrada é {}'.format (d, t, r))

#Resolução Guanabara
n = int(input('Digita um numero: \n'))
print('O dobro é {}, o triplo é {}, e a raíz quadrada é {:.2f}'.format ((n*2),(n*3),((n)**(1/2))))