#Desafio040
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#abaixo de 5.0 REPROVADO
#entre 5.0 e 6.9 RECUPERAÇÃO
#7.0 ou mais APROVADO

n1 = float(input('Digite sua P1 '))
n2 = float(input('Digite sua P2 '))
media = (n1+n2)/2 

if media < 5.0:
  print('REPROVADO')
elif media <= 6.9:
  print ('RECUPERAÇÃO')
else:
  print ('APROVADO')    
print(media) 

#Resolução Guanabara
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1+nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media>=5 and media<7:
  print('O aluno está em RECUPERAÇÃO')
elif media <5:
  print('O aluno está REPROVADO')  
elif media <=7  :
  print('O aluno está APROVADO')  