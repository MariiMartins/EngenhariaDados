#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas.
km = float(input('Digite a Quilometragem da Viagem '))
if km <=200:
    print('O valor foi de R$ {:.2f}'.format(km*.5))
else:
  print('Deu R$ {} o valor da viagem'. format(km*.45))

#Resolução Guanabara
distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
	preço = distancia * 0.50
else:
	preço = distancia * 0.45
print('e o preço da sua passagem será de R${:.2f}'.format(preço))

#Resolução 2
distancia = float(input('Qual é a distância da sua viagem? '))
preço = distância * 0.50 if distância <= 200 else distancia * 0.45
print('e o preço da sua passagem será de R${:.2f}'.format(preço))