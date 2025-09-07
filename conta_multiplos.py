'''
    Escreva um programa que receba como entrada dois números e retorne a quantidade 
    de números positivos menores que 50 que são múltiplos de ambos.
'''

num1 = int(input())
num2 = int(input())
cont=0

for i in range(1,50):
    if (i%num1==0) and (i%num2==0):
        cont+=1

print(cont)