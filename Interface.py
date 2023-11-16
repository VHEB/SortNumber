import tkinter as tk
from tkinter import messagebox

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
        #Inserindo valor
        self.lbl2 = tk.Label(self.frm1, text="Digite um Número:")
        self.lbl2.pack(side=tk.LEFT)
        self.ent = tk.Entry(self.frm1)
        self.ent.pack(side=tk.LEFT)
        self.btn = tk.Button(self.frm1, text="Conferir", command=self.Check)
        self.btn.pack()

    def Check(self):
        result =  self.ent.get()
        
             


ScreenMain = tk.Tk()
Screen(ScreenMain)


ScreenMain.mainloop()