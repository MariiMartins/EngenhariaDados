#Desafio 022
#Crie um programa que leia o nome completo da pessoa e mostre: 
#O nome com todas as letras maiusculas
#o Nome com todas as letras minusculas
# quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo '))
mai = nome.upper()
mi = nome.lower()
quantidade = len(nome)
letras = nome.split()
letras = [1:]
print(mai, mi, quantidade, letras)

#Resolução Guanabara
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print('Seu nome em Maiuscula é {} '.format(nome.upper()))
print('Seu nome em Minuscula é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format (nome.find(' ')))