'''
    Calcular os resultados totais de uma eleição com 3 candidatos, determinando o vencedor, 
    a validade da eleição e a necessidade de um segundo turno.
'''

total_a = total_b = total_c = total_brancos = total_nulos = 0
maior=0
candidato=''

while True:
    secao = int(input())
    if secao==0:
        break
    else:
        votos_A = int(input())
        votos_B = int(input())
        votos_C = int(input())
        votos_brancos = int(input())
        votos_nulos = int(input())
        total_a+=votos_A
        total_b+=votos_B
        total_c+=votos_C
        total_brancos+=votos_brancos
        total_nulos+=votos_nulos

if total_a>maior:
    maior=total_a
    candidato = 'A'
if total_b>maior:
    maior=total_b
    candidato = 'B'
if total_c>maior:
    maior=total_c
    candidato = 'C'
if total_a==total_b==total_c:
    candidato=''
    
votos_validos = total_a+total_b+total_c
tot_vot = total_a+total_b+total_c+total_brancos+total_nulos
bran_nul = total_brancos+total_nulos

if bran_nul<votos_validos:
    eleicao_valida = True
    x = 0.5*votos_validos
    if maior>x:
        seg_turno = False
    else:
        seg_turno = True
else:
    eleicao_valida = False
    seg_turno = False

print(f"Numero de votantes: {tot_vot}")
print(f"Total A: {total_a}")
print(f"Total B: {total_b}")
print(f"Total C: {total_c}")
print(f"Brancos: {total_brancos}")
print(f"Nulos: {total_nulos}")
print(f"Validos: {votos_validos}")
print(f"Candidato mais votado: {candidato}")
print(f"Eleicao valida? {eleicao_valida}")
print(f"Segundo turno? {seg_turno}")