#Desafio048
#Faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e que se encontram no intervalo de 1 até 500
soma = 0
for c in range(1, 501, 2):
	if c % 3 == 0:
		soma = soma + c
print ('A soma ed todos os números é {}'.format(soma))
