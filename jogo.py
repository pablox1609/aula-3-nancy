import random

numero_aleatorio = random.randint(0,10)
numero = -1
qtd_erros = 0
while numero != numero_aleatorio:
    numero = int(input("digite um numero"))
    if qtd_erros == 3:
        print("voce perdeu seu lixo")
        break
    else:
        if numero == numero_aleatorio:
            print("ganhei essa merda")
        else:
            print("voce errou burro")
            qtd_erros = qtd_erros + 1
print("o numero era ", numero_aleatorio)