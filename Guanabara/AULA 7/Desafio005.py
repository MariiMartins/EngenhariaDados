#Desafio 005
#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor
n1 = int(input('Digita um numero ae:\n '))
an = n1-1
sn = n1+1
print('Seu numero foi {}, o antecessor é {}, e o sucessor é {}'. format(n1,an, sn))

#Resolução Guanabara
n = int(input('Digita um numero: '))
print('Seu numero foi {}, o antecessor é {}, e o sucessor é {}'. format(n,(n-1),(n+1)))