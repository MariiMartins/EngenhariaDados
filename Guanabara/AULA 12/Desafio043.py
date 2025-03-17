#Desafio043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5: Abaixo do peso
#entre 18.5 e 25: pepso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

conta = peso/(altura**2)

if conta <18.5:
  print('Abaixo do Peso, seu IMC é de {:.2f}'.format(conta))
elif conta <25:
  print('Peso Ideal, seu IMC é de {:.2f}'.format(conta))
elif conta <30:
  print('Sobrepeso, seu IMC é de {:.2f}'.format(conta))
elif conta < 40:
  print ('Obesidade, seu IMC é de {:.2f}'.format(conta))
else:
  print('Obesidade Mórbida, seu IMC é de {:.2f}'.format(conta))


#Resolução Guanabara
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
if imc <18.5:
  print('ABAIXO DO PESO, seu IMC é de {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
  print('PESO IDEAL, seu IMC é de {:.2f}'.format(imc))
elif 25 <= imc < 30:
  print('SOBREPESO, seu IMC é de {:.2f}'.format(imc))
elif 30 <= imc < 40:
  print ('OBESIDADE, seu IMC é de {:.2f}'.format(imc))
elif imc >=40:
  print('OBESIDADE MORBIDA, seu IMC é de {:.2f}'.format(imc))  