#Desafio042
# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triânculo será formado
#EQUILATERIO: todos os lados iguais
#ISÓSCELES: dois lados iguais
#ESCALENO todos os lados diferentes

#Resolução Guanabara
r1 = int(input('Digite um comprimento '))
r2 = int(input('Digite um comprimento '))
r3 = int(input('Digite um comprimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print("Os segmentos acima PODEM formar um triângulo ", end='')
  if r1 == r2 == r3:
    print('EQUILATERO')
  elif r1 != r2 != r3!= r1:
    print ('ESCALENO')  
  else:
    print ('ISOCELES')  
else:
  print("Os segmentos NÃO PODEM formar triângulo")