from tkinter import messagebox

def MaiorOrMenor(Sort_value, User_value):
    if User_value > Sort_value:
        result = User_value - Sort_value
        messagebox.showinfo("Ajuda", "O número é menor que {}, \n A diferença entre o número Sorteado e o seu Palpite é de: {}".format(User_value, result +3))
  

    elif User_value < Sort_value:
        result = Sort_value - User_value
        messagebox.showinfo("Ajuda", "O número é maior que {}, \n A diferença entre o número Sorteado e o seu Palpite é de: {}".format(User_value, result +3))
   
def Quadrado(Sort_value, User_value):
    result = Sort_value * Sort_value
    #text = "O número sorteado é a Raiz de " , result
    messagebox.showinfo("Ajuda", "O número sorteado é a Raiz de {}".format(result))
    

def ParOrImpar(Sort_value, User_value):
    if Sort_value % 2 == 0:
        messagebox.showinfo("Ajuda","O número sorteado é Par!")
    else:
        messagebox.showinfo("Ajuda","O número sorteado é Impar!")
    