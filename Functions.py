def MaiorOrMenor(Sort_value, User_value):
    if User_value > Sort_value:
        result = User_value - Sort_value
        print("Errou, o número é menor que " , User_value)
        print("A diferença entre o número Sorteado e o seu Palpite é de: " , result + 3, " mais ou menos ;)")
    elif User_value < Sort_value:
        result = Sort_value - User_value
        print("Errou, o número é maior que " , User_value)
        print("A diferença entre o número Sorteado e o seu Palpite é de: " , result + 3, " mais ou menos ;)")
   
def Quadrado(Sort_value, User_value):
    result = Sort_value * Sort_value
    print("O número sorteado é a Raiz de " , result)

def ParOrImpar(Sort_value, User_value):
    if Sort_value % 2 == 0:
        print("O número Sorteado é par!")
    else:
        print("O número Sorteado é Impar")
    