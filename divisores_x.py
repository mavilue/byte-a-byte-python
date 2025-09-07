'''
    Escreva um programa que receba como entrada um número inteiro positivo 
    e exiba todos os divisores positivos dele em ordem decrescente.
'''

x = int(input())

for i in range(x,0,-1):
    if (x%i==0):
        print(i)