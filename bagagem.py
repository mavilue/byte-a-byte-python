''' Cálculo da taxa de excesso de bagagem com base no peso informado '''

peso_bag = float(input())
taxa = 0

if peso_bag<=20:
    print(f"{taxa:.2f}")

elif peso_bag<=25:
    taxa = (peso_bag-20)*12.50
    print(f"{taxa:.2f}")

elif peso_bag<=30:
    taxa = (peso_bag-20)*32.75
    print(f"{taxa:.2f}")

else:
    print("PESO LIMITE EXCEDIDO")