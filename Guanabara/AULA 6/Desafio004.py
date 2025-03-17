#Desafio004 Faça um programa que leia algo pelo teclado e seu tipo primitivo e todas as informações possiveis sobre ele.
##Resolução Guanabara
a = input("Digita algo ae: ")
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiusculas? ',a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())