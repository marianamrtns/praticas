import forca
import Adivinhacao

def escolha_jogo():
    print("********************************")
    print("******Escolha o seu jogo!*******")
    print("********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você quer jogar?"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        Adivinhacao.jogar_adivinhacao()
if (__name__ == "__main__"):
    escolha_jogo()



