import random

def jogar_adivinhacao():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    num_secreto = random.randrange(1, 51)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual é o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nível = int (input("Defina o nível:"))

    if (nível == 1):
        total_tentativas = 20
    elif (nível == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range (1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um número entre 1 e 50: ")
        numero = int(chute)

        print("Você digitou", chute)

        if (numero < 1 or numero > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        acertou = num_secreto == numero
        maior   = numero > num_secreto
        menor   = numero < num_secreto


        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(num_secreto - numero)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo!")
    print("O número era", num_secreto)

if(__name__ =="__main__"):
    jogar_adivinhacao()