# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:21:53 2020

@author: felix
"""
import tkinter as tk
from random import choice, randrange

class Gameboard:
    
    def __init__(self, canvas_width, canvas_height):
        self.root = tk.Tk()
        
        self.board_width=canvas_width
        self.board_height=canvas_height
        self.board_lineDist=0
        
        self.board = tk.Canvas(self.root, width=self.board_width, height=self.board_height)
        
        self.gameelements = Gameelements(self,self.board)
        
#        self.snake = self.board.create_rectangle(0, 0, 10, 10, outline="#fb0", fill='blue')
        self.snakeTest = Snake(self.board,0, 0, 10, 10, self.gameelements)
        

        self.label = tk.Label(self.board, fg = 'green')
        self.label.config(text = str(self.snakeTest.length))
        self.label.pack()
 
        
        self.checkered(10)
        self.createButtons()
        self.board.pack(fill=tk.BOTH, expand=1)
        
        
        tk.mainloop()
        
    def __call__(self):
        print(self.board_height)

    def checkered(self, line_distance):
        self.board_lineDist=line_distance
           # vertical lines at an interval of "line_distance" pixel
        for x in range(line_distance,self.board_width,line_distance):
            self.board.create_line(x, 0, x, self.board_height, fill="#476042")
           # horizontal lines at an interval of "line_distance" pixel
        for y in range(line_distance,self.board_height,line_distance):
            self.board.create_line(0, y, self.board_width, y, fill="#476042")

        
    def createButtons(self):
  
        button_moveSnakeLeft = tk.Button(self.board,text="L",command=lambda: self.snakeMove([-1,0,-1,0]), height=1, width=7)
        button_moveSnakeLeft.pack(side="right")
        button_moveSnakeRight = tk.Button(self.board,text="R",command=lambda: self.snakeMove([1,0,1,0]), height=1, width=7)
        button_moveSnakeRight.pack(side="right")
        button_moveSnakeUp = tk.Button(self.board,text="U",command=lambda: self.snakeMove([0,-1,0,-1]), height=1, width=7)
        button_moveSnakeUp.pack(side="right")
        button_moveSnakeDown = tk.Button(self.board,text="D",command=lambda: self.snakeMove([0,1,0,1]), height=1, width=7)
        button_moveSnakeDown.pack(side="right")
             
    def buttonMove(self,drct):
        shift=[x * self.board_lineDist for x in drct]
        crdnts=self.board.coords(self.snake)
        self.board.coords(self.snake,crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3])

    def snakeMove(self,drct):
        self.snakeTest=self.snakeTest.move(drct)
        

class Snake:
    
    def __init__(self,board,i,j,k,l,gameelements,precessor = None, succesor = None, length: int = 5):
        self.board = board
        self.element = self.board.create_rectangle(i, j, k, l, outline="#fb0", fill='blue')
        self.precessor = precessor
        self.succesor = succesor
        self.lastDrct = [0,0,0,0]
        self.length = length
        self.coords = [i,j,k,l]
        self.gameelements = gameelements

    def move(self,drct):
        if self.precessor != None:
            self.precessor.move(drct)
        # prohibits backwards movement
        if self.lastDrct == [-1*i for i in drct]:
            return self
        else:
            shift=[x * 10 for x in drct]
            crdnts=self.board.coords(self.element)
            self.gameelements.collision([crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3]])
            if self.collison([crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3]]):
                print('!COLLISON!')
            self.precessor = Snake(self.board,crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3],self.gameelements,succesor=self,length=self.length-1)
            self.precessor.lastDrct=drct
            if self.length <= 0:
                self.delete()
            return self.precessor 
            
                                    
    def delete(self):
        if self.succesor == None and self.precessor != None:
            self.precessor.succesor = None
            self.board.delete(self.element)
            del self
        else:
            self.succesor.delete()
            
    def add(self):
        if self.succesor == None:
            shift=[x * -10 for x in self.lastDrct]
            crdnts=self.board.coords(self.element)
            self.succesor = Snake(self.board,crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3],self.gameelements,precessor=self,succesor=None,length=self.length)
        else:
            self.succesor.add()
            
    def collison(self,crds):
        if self.succesor == None and self.coords != crds:
            return False
        if  self.coords == crds:
            return True
        else:
            return self.succesor.collison(crds)
            

#class Gameelements represents all obstacles and gadgetd which can be collected on the gameboard                   
class Gameelements:
    
    def __init__(self,gameboard,board):
        self.gameboard=gameboard
        self.board = board
        self.fruits = [Fruit(self.board) for i in range(4)]
        self.fruitCount = 0
        
    def count(self):
        return self.gameboard.snakeTest.length
        
    def collision(self, crds):
        for i in self.fruits:
            if i.cords == crds:
                print('EATING A FRUIT')
                i.remove()
                self.fruitCount = self.fruitCount + 1
                self.gameboard.label.config(text = str(self.count()))
                self.gameboard.snakeTest.add()
            

        

class Fruit:
    
    def __init__(self,board):
        self.board = board
        self.color = choice(['blue','red','green'])
        self.cords, self.element = self.create()

    def create(self):
        [i,j]=[randrange(10,100,10) for i in range(2)] 
        return [i,j,i+10,j+10],self.board.create_rectangle(i, j, i+10, j+10, outline="#fb0", fill='green')
               
    def remove(self):
        self.board.delete(self.element)


if __name__ == '__main__':
    SnakeCanvas = Gameboard(1000,500)
    

# collision function needs correct counting function