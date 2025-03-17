#Desafio056
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idaade do grupo
#Qual é o nome do homem mais velho.
#Qauntas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade =0
maidadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
  print('----{}----'. format(p))
  nome = str(input('Nome ')).strip()
  idade = int(input('Idade '))
  sexo = str(input('[M/F] ')).strip()
  somaidade += idade
  if p ==1 and sexo in 'Mm':
    maidadehomem = idade
    nomevelho = nome
  if sexo in 'Mm'  and idade > maidadehomem:
    maidadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:  
    totmulher20 +=1

mediaidade = somaidade /4
print('A média idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maidadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
