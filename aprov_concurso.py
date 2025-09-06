'''
    Escreva um programa que leia os acertos em português (50), matemática (35)
    e a nota da redação de cada candidato, 
    e exiba quantos foram aprovados (≥80% em português, ≥60% em matemática e redação ≥7).
'''

lim_pt = (50*80)/100 #40
lim_mat = (35*60)/100 #21
red = 7
cont = 0

while True:
    acerto_pt = int(input())
    if (acerto_pt<0):
        break

    else:
        acerto_mat = int(input())
        nota_red = float(input())

        if (acerto_pt>=lim_pt) and (acerto_mat>=lim_mat) and (nota_red>=red):
          cont += 1
  
print(cont)