import tkinter as tk
from tkinter import messagebox
import Functions
import random

introText = "Olá, meu nome é Vitor Hugo \n Esse é meu primeiro projeto em Pyhton \n SORT NUMBER \n"
objText = "Seu objetivo caro jogador é descobrir o Número que foi gerado aleatoriamente. \n Boa Sorte \n"


class Screen:
    def __init__(self,master):
        self.YourScreen = master
        self.YourScreen.title("SortNumber")
        #frame 0
        self.frm = tk.Frame()
        self.frm.pack()
        #frame 1
        self.frm1 = tk.Frame()
        self.frm1.pack()
        #---------------------------------------------------#
        #Texto de Apresentação
        self.lbl = tk.Label(self.frm, text=introText)
        self.lbl.pack()
        #Texto Explicativo
        self.lbl1 = tk.Label(self.frm, text=objText)
        self.lbl1.pack()

        #Gerando um número
        self.btn = tk.Button(self.frm, text="Gerar Número", command=self.Gerar)
        self.btn.pack()

        #Inserindo valor
        self.lbl2 = tk.Label(self.frm1, text="Digite um Número:")
        self.lbl2.pack(side=tk.LEFT)
        self.ent = tk.Entry(self.frm1)
        self.ent.pack(side=tk.LEFT)
        self.btn1 = tk.Button(self.frm1, text="Conferir", command=self.Check)
        self.btn1.pack(pady=20)

        
    def Gerar(self):
        global Sort_Num 
        Sort_Num = random.randint(0,100)
        messagebox.showinfo("Alerta","Número gerado entra 0 e 100! \n Boa Sorte")
        print(Sort_Num)
    
    def Check(self):
        
        #Try_User += 1
        try:
            User_Num =  int(self.ent.get())
            if User_Num == Sort_Num:
                messagebox.showinfo("Alerta", "Meus Parabês você Acertou!" )
            else:
                i = random.randint(0,2)
                if i == 0:
                    Functions.MaiorOrMenor(Sort_Num,User_Num)
                elif i == 1:
                    Functions.ParOrImpar(Sort_Num,User_Num)
                else:
                    Functions.Quadrado(Sort_Num,User_Num) 
    
        except ValueError as err:
            messagebox.showinfo("Erro","Valor Digitado invalido!")
            
               

        






ScreenMain = tk.Tk()
Screen(ScreenMain)


ScreenMain.mainloop()