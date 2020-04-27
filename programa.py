#Escolha de uma opção
import random

print("Menu: \n (1) Abrir Netflix\n (2) Abrir Amazon Prime\n (3) Abrir HBO GO\n (4) Sair")
menu = int(input("Escolha uma opção:"))
print("Sua opção: {}".format(menu))

if  (menu == 1):
    print("OK! Abrir Netflix!")
elif (menu == 2):
    print("OK! Abrir Amazon Prime!")
elif (menu == 3):
    print("OK! Abrir HBO GO!")
elif (menu == 4):
    print("Saindo do menu...")
else:
    print("Opção inválida!")