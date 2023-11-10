#Aplicação que vai sortear um número e o usúario tentará acerta-lo

import random
import os
import Functions

#Aqui Sorteia O NÚMERO
Sort_Num = random.randint(0,10)
Burn = [2,3,4,5]
Sort_Burn = random.choice(Burn)
User_Num = 0

#Texto Introdutorio
print("Olá, meu nome é Vitor Hugo \n Esse é meu primeiro projeto em Pyhton \n SORT NUMBER \n")
print("Seu objetivo caro jogador é descobrir o Número que foi gerado aleatoriamente. \n Boa Sorte \n")

#Vamos para a lógica

#Aqui o Usúario adiciona um Número
User_Num = int(input("Digite um Número: "))

if Sort_Num != User_Num:
    while Sort_Num != User_Num:    
        if Sort_Num < User_Num:
            if Functions.Somar(User_Num, Sort_Burn) == Sort_Num:
                os.system('cls')
                print("Está Quente! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            elif Functions.Somar(User_Num, Sort_Burn*2) == Sort_Num:
                os.system('cls')
                print("Está Morno! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            elif Functions.Somar(User_Num, Sort_Burn*3) == Sort_Num:
                os.system('cls')
                print("Está Frio! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            else:
                os.system('cls')
                print("Glacial \n")
                User_Num = int(input("Digite um Número Novamente: \n"))

        elif Sort_Num > User_Num:
            if Functions.Subtracao(User_Num, Sort_Burn) == Sort_Num:
                os.system('cls')
                print("Está Quente! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            elif Functions.Subtracao(User_Num, Sort_Burn*2) == Sort_Num:
                os.system('cls')
                print("Está Morno! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            elif Functions.Subtracao(User_Num, Sort_Burn*3) == Sort_Num:
                os.system('cls')
                print("Está Frio! \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
            else:
                os.system('cls')
                print("Glacial \n")
                User_Num = int(input("Digite um Número Novamente: \n"))
                
elif Sort_Num == User_Num:
    print("Meus Parbêns você conseguiu!")
else:
    print("Por Favor Digite um Número Inteiro.")

