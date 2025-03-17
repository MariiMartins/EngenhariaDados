#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de duas pelos quais ele foi alugadi. Calcule o preço a pagar, sabendo que oo carro custa R$60 por dia e R$0,15 por km rodado
qkm = float(input('Qual a quantidade de KM percorridos pelo carro? \n'))
qd = int(input('Qual a quantidade de dias que o carro foi alugado? \n'))

v=(qd*60) + (.15*qkm)

print('Vai ter que pagar R$ {}'.format(v))