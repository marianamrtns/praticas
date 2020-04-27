numero = int(input("Digite o número:"))

total_tentativas = 10
rodada = 1
total = numero * rodada

while (rodada <= total_tentativas):
    print("{} x {} = {}".format(numero, rodada, total))
    rodada = rodada + 1
    total = numero * rodada
else:
    print("Fim")
