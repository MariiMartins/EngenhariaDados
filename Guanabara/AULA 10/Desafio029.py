#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem deizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite
vel=float(input('Digite a velocidade do carro: '))
if vel >80:
  m = ((vel-80)*7)
  print('Você foi multado em R$ {:.2f} pois o limite é de 80Km/h'. format(m))
else:
  print('Bom motorista')  

#Resolução Guanabara  
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
  print ('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
  multa = (velocidade-80)*7
  print('Você deve pagar uma multa de R$ {:.2f}!'. format(multa))
print ('Tenha um bom dia! Dirija com segurança!')
