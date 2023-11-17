from tkinter import messagebox

def MaiorOrMenor(Sort_value, User_value):
    if User_value > Sort_value:
        result = User_value - Sort_value
        text = " O número é menor que " , User_value , "\n A diferença entre o número Sorteado e o seu Palpite é de: " , result + 3, " \n mais ou menos ;)"
        messagebox.showinfo("Ajuda", text)

    elif User_value < Sort_value:
        result = Sort_value - User_value
        text = " O número é maior que " , User_value , "\n A diferença entre o número Sorteado e o seu Palpite é de: " , result + 3, " \n mais ou menos ;)"
        messagebox.showinfo("Ajuda", text)
   
def Quadrado(Sort_value, User_value):
    result = Sort_value * Sort_value
    text = "O número sorteado é a Raiz de " , result
    messagebox.showinfo("Ajuda", text)
    

def ParOrImpar(Sort_value, User_value):
    if Sort_value % 2 == 0:
        messagebox.showinfo("Ajuda","O número sorteado é Par!")
    else:
        messagebox.showinfo("Ajuda","O número sorteado é Impar!")
    