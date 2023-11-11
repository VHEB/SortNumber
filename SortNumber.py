#Aplicação que vai sortear um número e o usúario tentará acerta-lo

import random
import os
import Functions

#Aqui Sorteia O NÚMERO
Sort_Num = random.randint(0,100)
Try_User = 0
User_Num = 0

#Texto Introdutorio
print("Olá, meu nome é Vitor Hugo \n Esse é meu primeiro projeto em Pyhton \n SORT NUMBER \n")
print("Seu objetivo caro jogador é descobrir o Número que foi gerado aleatoriamente. \n Boa Sorte \n")


while User_Num is not Sort_Num:
    
    Try_User += 1
   
    try:
        User_Num = int(input("Adivinhe o Número: "))
        os.system('cls')
        if User_Num == Sort_Num:
            print("Meus Parabês você Acertou! O número era " , Sort_Num , " e levou apenas " , Try_User , " tentativas.")
        else:
            i = random.randint(0,2)
            if i == 0:
                Functions.MaiorOrMenor(Sort_Num,User_Num)
            elif i == 1:
                Functions.ParOrImpar(Sort_Num,User_Num)
            else:
                Functions.Quadrado(Sort_Num,User_Num) 
    except ValueError:
        print("Valor Digitado invalido.")




