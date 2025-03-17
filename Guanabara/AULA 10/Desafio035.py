#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = int(input('Digite um comprimento '))
r2 = int(input('Digite um comprimento '))
r3 = int(input('Digite um comprimento '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triângulo")
else:
    print("Os segmentos acima não podem formar triângulo")

#Resolução Guanabara    
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite um comprimento '))
r2 = float(input('Digite um comprimento '))
r3 = float(input('Digite um comprimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triângulo")
else:
    print("Os segmentos acima não podem formar triângulo")