#!/usr/bin/python

import random
import tkinter

top = tkinter.Tk()

w = tkinter.Canvas( top, bd = 10, bg = 'black', height =  425, width = 650 )


mid_line = 325, 0, 325, 450
paddle_1 = 585, 182, 585, 242
paddle_2 = 65, 182, 65, 242
rectangle = w.create_polygon( mid_line, outline ='gray', fill = 'gray', width = 8)
paddle1 = w.create_polygon( paddle_1, outline ='gray', fill = 'gray', width = 8)
paddle2 = w.create_polygon( paddle_2, outline ='gray', fill = 'gray', width = 8)


w.pack()
top.mainloop()