''' 
    Uma caixa com 12 pregos custa R$ 7,89. 
    Dada a quantidade de pregos necessários, calcule o valor gasto e quantos pregos sobrarão 
'''

valor = 7.89
caixa_prego = 12
total_pregos = 0

while True:
    num = int(input())
    if num % 2 != 0:
        break
    total_pregos += num

if total_pregos % caixa_prego == 0:
    caixas = total_pregos // caixa_prego
else:
    caixas = total_pregos // caixa_prego + 1

valor_gasto = caixas * valor
sobra = (caixas * caixa_prego) - total_pregos

print(f"R$ {valor_gasto:.2f}")
print(sobra)