#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
n1 = int(input('Digita um numero ae '))
n2 = int(input('Digita outro numero ae '))
n3 = int(input('Digita o terceiro numero ae '))
maior = n1
if (n2 > maior):
  maior = n2
if (n3 > maior):
  maior = n3
print('Maior: ',maior)

menor = n1
if (n2 < menor):
  menor = n2
if (n3 < menor):
  menor = n3
print('Menor: ',menor)

#Resolução Guanabara
a = int(input('Digita um numero ae '))
b = int(input('Digita outro numero ae '))
c = int(input('Digita o terceiro numero ae '))
menor = a
if b < a and b < c:
	menor = b
if c < a and c < b:
	menor = c
print('O menor valor digitado é {}'.format(menor))

maior = a
if b > a and b > c:
	maior = b
if c > a and c > b:
	maior = c
print('O maior valor digitado é {}'.format(maior))
