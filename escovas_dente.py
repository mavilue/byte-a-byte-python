'''
Calcule quanto Vicente gastará comprando escovas de dente para todos os alunos de uma creche, 
considerando a promoção “compre 2, leve 3”.
'''

qnt_alunos = int(input())
total = 0
unid_escova = 2.20
cont = 0

for i in range(1,qnt_alunos+1):
    cont += 1
    if cont % 3 == 0:
        pass
    else:
        total += unid_escova    

print(f"{total:.2f}")