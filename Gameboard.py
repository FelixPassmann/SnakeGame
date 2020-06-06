# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:21:53 2020

@author: felix
"""
import tkinter as tk

class Gameboard:
    
    def __init__(self, canvas_width, canvas_height):
        self.root = tk.Tk()
        
        self.board_width=canvas_width
        self.board_height=canvas_height
        self.board_lineDist=0
        
        self.board = tk.Canvas(self.root, width=self.board_width, height=self.board_height)
        
#       self.snake = self.board.create_rectangle(0, 0, 10, 10, outline="#fb0", fill='blue')
        self.snake = Snake(self.board,0, 0, 10, 10)
 
        
        self.checkered(10)
        self.setSquare(20,20)
        self.createButtons()
        
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

    def setSquare(self,i,j):
        self.board.create_rectangle(i, j, i+10, j+10, outline="#fb0", fill="#fb0")
        self.board.pack(fill=tk.BOTH, expand=1)
        
    def createButtons(self):
        button_moveLeft = tk.Button(self.board,text="L",command=lambda: self.buttonMove([-1,0,-1,0]), height=1, width=7)
        button_moveLeft.pack(side="right")
        button_moveRight = tk.Button(self.board,text="R",command=lambda: self.buttonMove([1,0,1,0]), height=1, width=7)
        button_moveRight.pack(side="right")
        button_moveUp = tk.Button(self.board,text="U",command=lambda: self.snake.move([0,-1,0,-1]), height=1, width=7)
        button_moveUp.pack(side="right")
        button_moveDown = tk.Button(self.board,text="D",command=lambda: self.buttonMove([0,1,0,1]), height=1, width=7)
        button_moveDown.pack(side="right")
        
    def buttonMove(self,drct):
        shift=[x * self.board_lineDist for x in drct]
        crdnts=self.board.coords(self.snake)
        self.board.coords(self.snake,crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3])



class Snake:
    
    def __init__(self,board,i,j,k,l,precessor = None, succesor = None):
        self.board = board
        self.element = self.board.create_rectangle(i, j, k, l, outline="#fb0", fill='blue')
        self.precessor = precessor
        self.succesor = succesor

    def move(self,drct):
        if self.precessor != None:
            self.precessor.move(drct)
        else:
            shift=[x * self.board_lineDist for x in drct]
            crdnts=self.board.coords(self.snake)
            self.precessor = Snake(self.board,crdnts[0]+shift[0],crdnts[1]+shift[1],crdnts[2]+shift[2],crdnts[3]+shift[3],succesor=self)
               
            
        self.succesor.delete()
                                    
    def delete(self):
        if self.succesor == None & self.precessor != None:
            self.precessor.precessor = None
            self.board.delete(self.element)
        else:
            self.succesor.delete()
                      
        
        

if __name__ == '__main__':
    SnakeCanvas = Gameboard(1000,500)
    
    
    
 

    


        

       

