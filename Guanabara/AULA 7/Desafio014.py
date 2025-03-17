#Resolução Guanabara | Não teve enunciado anterior
c = float(input('Digite a temperatura em ºC '))
ke = float(c + 273.15)
f = float(c * (9 / 5) + 32)

print('A temperatura {} °C, corresponde a {} °F e a {} °K'.format(c, f, ke))