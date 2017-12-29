#! /usr/bin/env python3
# coding: utf-8


"""
===== main.py =====

The main file.

"""


import tkinter
import colorsLog as clg     #colorsLog is a module available on https://github.com/LopsemPyier/colorsLog. You need install the colors module after. He is available on https://github.com/LopsemPyier/colors.


def power(num, exposant = 2):     #The function to calculate the power of a number.
	"""
	Function to calculate a power.
	Requested settings :
	 - The number (num) requisite.
	 - The power (exposant) optionnal, default value : 2
	"""
	if not type(num) == int:
		num = int(num)
	out = 1
	if exposant > -1:
		for loop in range(exposant):
			clg.debug(out)
			out *= num
		return out
	elif exposant < 0:
		return 1 / power(num, -exposant)

class Display():     #Class to display the widgets.
	def __init__(self, win):

		#===== Frames =====
		self.window = win
		self.titre = tkinter.Label(self.window, text = "Power calculator").pack()
		self.enter = tkinter.Frame(self.window)
		self.numPuis = tkinter.Frame(self.enter)
		self.expLab = tkinter.Frame(self.enter)
		self.bottun = tkinter.Frame(self.window)
		self.resultFra = tkinter.Frame(self.window)

		#===== Widgets =====
		self.labNum = tkinter.Label(self.numPuis, text = "The number to put in power (a) : ")
		self.num = tkinter.StringVar()
		self.numEnt = tkinter.Entry(self.numPuis, textvariable = self.num, width = 30)
		self.labExp = tkinter.Label(self.expLab, text = "The power (b) : ")
		self.exp = tkinter.StringVar()
		self.expEnt = tkinter.Entry(self.expLab, textvariable = self.exp, width = 30)
		self.go = tkinter.Button(self.bottun, text = "Calculate", command = self.calcul)
		self.res = tkinter.Button(self.bottun, text = "Reset", command = self.reset)
		self.resultLab = tkinter.Label(self.resultFra, text = "a power b = ")
		self.resul = tkinter.StringVar()
		self.result = tkinter.Entry(self.resultFra, textvariable = self.resul)
		self.quitt = tkinter.Button(self.window, text = "Quit", command = self.window.quit)
		self.errorNum = tkinter.Label(self.numPuis, text = "Please enter a number", fg = "red")
		self.errorExp = tkinter.Label(self.expLab, text = "Please enter a integer number", fg = "red")

		#===== Display the Widgets and the Frames =====
		self.numPuis.pack(side = "top")
		self.expLab.pack(side = "bottom")
		self.enter.pack()
		self.bottun.pack()
		self.resultFra.pack()
		self.labNum.pack(side = "left")
		self.numEnt.pack(side = "right")
		self.labExp.pack(side = "left")
		self.expEnt.pack(side = "right")
		self.go.pack(side = "left")
		self.res.pack(side = "right")
		self.resultLab.pack(side = "left")
		self.result.pack(side = "right")
		self.quitt.pack()
		self.resul.set("c")

	def calcul(self):     #Calculate function.
		#===== Check of number's validity =====
		try :
			self.resu = power(float(self.num.get()), int(self.exp.get()))
		except ValueError :
			try :
				float(self.num.get())
			except ValueError :
				self.errorNum.pack(side = "left")     #Display error message
			else :
				self.errorNum.pack_forget()
			try :
				int(self.exp.get())
			except ValueError :
				self.errorExp.pack(side = "left")     #Display error message
			else :
				self.errorExp.pack_forget()
		else :
			self.errorNum.pack_forget()
			self.errorExp.pack_forget()
			self.resultLab["text"] = "{} power {} = ".format(self.num.get(), self.exp.get())     #Update the text
			self.resul.set(str(self.resu))     #Display the resultat
			self.result["width"] = len(str(self.resu)) + 1
			clg.debug(self.resu)

	def reset(self):     #Reset function. Put the default value on Widgets.
		self.resultLab["text"] = "a power b = "
		self.num.set("")
		self.exp.set("")
		self.resul.set("c")
		self.result["width"] = 30
		self.errorNum.pack_forget()
		self.errorExp.pack_forget()

#clg.debugLevel()
tk = tkinter.Tk()
dicplay = Display(tk)
tk.title("Power calculator")
tk.mainloop()
