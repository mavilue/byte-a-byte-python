'''
Escreva um programa que leia pH de várias soluções até -1 e exiba se cada uma é ACIDA (pH < 7), BASICA (pH > 7) ou NEUTRA (pH = 7).
'''

lista = []

while True:
    solucao_ph = float(input())

    if solucao_ph==-1:
        break 

    else:
        if solucao_ph<7:
            acidez = 'ACIDA'
        elif solucao_ph>7:
            acidez = 'BASICA'
        else:
            acidez = 'NEUTRA'
        
        lista.append(acidez)
 
for i in lista:
    print(i)
            