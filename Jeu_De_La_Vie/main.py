import tkinter
import numpy as np
import copy
import time
import random

class LifeGame():
    def __init__(self):
        self.tk = tkinter.Tk()
        self.can = tkinter.Canvas(self.tk, bg="White", height=500, width=500)
        self.can.grid(row=0)
        self.can2 = tkinter.Canvas(self.tk, bg="White", height=100, width=500)
        self.can2.grid(row=1)
        self.grill = np.zeros((100,100))
        self.grill_init = np.zeros((100,100))
        self.pattern = {}
        self.init_pattern()
        self.chosen_pat = ""
        self.init_grill()
        self.color = ["red", "blue", "yellow", "green"]
        self.can.bind('<Button-1>', self.colorClick)
        B1 = tkinter.Button(self.can2, text='Go', command=self.golavie2)
        B1.grid(row=0, column=0)
        B2 = tkinter.Button(self.can2, text='Reset', command=self.Reset)
        B2.grid(row=0, column=1)
        B3 = tkinter.Button(self.can2, text='Planeur', command=self.planneur)
        B3.grid(row=0, column=2)
        B4 = tkinter.Button(self.can2, text='Expl', command=self.Expl)
        B4.grid(row=0, column=3)
        self.tk.mainloop()

    def colorClick(self, evt):
        x = evt.x//5
        y = evt.y//5
        if self.chosen_pat != "":
            dim = self.pattern[self.chosen_pat].shape
            for i in range(dim[0]):
                for j in range(dim[1]):
                    if self.grill[x+i, y+j] == 0 and self.pattern[self.chosen_pat][i,j] == 1:
                        self.grill[x + i, y + j] = 1
                        self.place_point(x+j, y+i, "Black")
                    elif self.grill[x+i, y+j] == 1 and self.pattern[self.chosen_pat][i,j] == 0:
                        self.grill[x + i, y + j] = 0
                        self.place_point(x+i, y+j, "White")
        else:
            if self.grill[x,y] == 0:
                self.place_point(x,y, "Black")
                self.grill[x,y] = 1
            else:
                self.place_point(x,y, "White")
                self.grill[x,y] = 0

    def init_grill(self):
        for i in range(100):
            self.can.create_line(0, i*5, 500, i*5)
        for i in range(100):
            self.can.create_line(i*5, 0, i*5, 500)
        for i in range(100):
            for j in range(100):
                if self.grill[i,j] == 1:
                    self.place_point(i,j,random.choice(self.color))

    def init_pattern(self):
        self.pattern["planneur"] = np.array([[0,1,0],[0,0,1],[1,1,1]])
        self.pattern["Expl"] = np.array([[0,1,0,0],[1,1,1,0],[1,0,1,1], [1,1,1,0], [0,1,0,0]])

    def planneur(self):
        self.chosen_pat = "planneur"

    def Expl(self):
        self.chosen_pat = "Expl"

    def Reset(self):
        self.can.delete("all")
        self.go = False
        for i in range(100):
            self.can.create_line(0,i*5,500,i*5)
        for i in range(100):
            self.can.create_line(i*5,0,i*5,500)
        for i in range(100):
            for j in range(100):
                if self.grill_init[i,j] == 1:
                    self.place_point(i,j,random.choice(self.color))
        self.grill = self.grill_init
        self.tk.update()

    def place_point(self, x, y, col):
        self.can.create_rectangle(x*5, y*5, (x*5) + 5, (y*5)+5, fill=col)

    def golavie(self):
        for i in range(1):
            grill2 = copy.copy(self.grill)
            for i in range(1,99):
                for j in range(1,99):
                    L = [self.grill[i-1,j-1], self.grill[i-1,j], self.grill[i,j-1], self.grill[i+1,j], self.grill[i,j+1], self.grill[i+1,j+1], self.grill[i-1,j+1], self.grill[i+1,j-1]]
                    countLife = L.count(1)
                    if countLife == 3:
                        self.place_point(i, j, random.choice(self.color))
                        grill2[i, j] = 1
                    elif countLife == 2:
                        pass
                    else:
                        self.place_point(i, j, "White")
                        grill2[i, j] = 0
            self.grill = grill2
        self.can.delete("all")
        self.init_grill()
        self.tk.update()

    def golavie2(self):
        self.grill_init = self.grill
        self.go = True
        i = 0
        while self.go == True:
            self.golavie()
            i+=1


lg = LifeGame()