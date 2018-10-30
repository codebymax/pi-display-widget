import random
from tkinter import font
import tkinter
#import foodBot
import weatherBot

class UIGenerate():
	top = tkinter.Tk()

	w = tkinter.Canvas( top, bd = 10, bg = '#03242E', height =  480, width = 800 )

	def boxMaker( unit, topX, topY, botX, botY, color ):
		points = topX, topY, botX, topY, botX, botY, topX, botY
		return unit.create_polygon( points, fill = color)
	#points = 10, 10, 280, 10, 280, 170, 10, 170
	#rectangleNW = w.create_polygon( points, fill = 'gray')
	rectangleNW = boxMaker( w, 10, 10, 170, 280, "#1080A0")
	rectangleNE = boxMaker( w, 190, 10, 470, 280, "#1080A0")
	Impact15 = font.Font( family='Impact', size=15 )
	phraseObj = w.create_text( 77, 20, font = Impact15, text = "Weather is " + weatherBot.phrase )
	tempObj = w.create_text( 33, 40, font = Impact15, text = weatherBot.temp + "F" )
	rainObj = w.create_text( 60, 60, font = Impact15, text = weatherBot.rain_chance + " precip" )
	feelObj = w.create_text( 70, 80, font = Impact15, text = "Feels like " + weatherBot.feels_like )
	humidityObj = w.create_text( 50, 100, font = Impact15, text = weatherBot.humidity )
	w.pack()
	top.mainloop()

