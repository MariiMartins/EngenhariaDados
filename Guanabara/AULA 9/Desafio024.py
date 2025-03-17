#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = str(input('Digite sua Cidade: ')).upper().strip()
cid = 'SANTO' in cidade
print (cid)

#Resolução Guanabara
cid = str(input('Digite sua Cidade: ')).strip()
print (cid[:5].upper() == 'SANTO')