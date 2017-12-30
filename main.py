#! /usr/bin/env python3
# coding: utf-8


"""
===== main.py =====

The main file.

"""


import time
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
		self.resultLab = tkinter.Label(self.resultFra, text = "a ^ b = ")
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
		with open(filePath, "a") as f:
			f.write("[{}] : Begining of calculation;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))
		with open(filePath, "a") as f:
			f.write("[{}] : Calculation of '{}' ^ '{}';\n".format(time.strftime("%A %d %B %Y at %H:%M:%S"), self.num.get(), self.exp.get()))
		#===== Check of number's validity =====
		try :
			self.resu = power(float(self.num.get()), int(self.exp.get()))
		except ValueError :
			with open(filePath, "a") as f:
				f.write("[{}] : ValueError;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))
			try :
				float(self.num.get())
			except ValueError :
				self.errorNum.pack(side = "left")     #Display error message
				with open(filePath, "a") as f:
					f.write("[{}] : The number is not a number;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))
			else :
				self.errorNum.pack_forget()
			try :
				int(self.exp.get())
			except ValueError :
				self.errorExp.pack(side = "left")     #Display error message
				with open(filePath, "a") as f:
					f.write("[{}] : The power is not a integer number;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))
			else :
				self.errorExp.pack_forget()
		else :
			self.errorNum.pack_forget()
			self.errorExp.pack_forget()
			self.resultLab["text"] = "{} ^ {} = ".format(self.num.get(), self.exp.get())     #Update the text
			self.resul.set(str(self.resu))     #Display the resultat
			self.result["width"] = len(str(self.resu)) + 1
			with open(filePath, "a") as f:
				f.write("[{}] : The resultat is {};\n".format(time.strftime("%A %d %B %Y at %H:%M:%S"), self.resu))
			clg.debug(self.resu)
		with open(filePath, "a") as f:
			f.write("[{}] : End of calculation;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))

	def reset(self):     #Reset function. Put the default value on Widgets.
		with open(filePath, "a") as f:
			f.write("[{}] : Reset Widgets;\n".format(time.strftime("%A %d %B %Y at %H:%M:%S")))
		self.resultLab["text"] = "a ^ b = "
		self.num.set("")
		self.exp.set("")
		self.resul.set("c")
		self.result["width"] = 30
		self.errorNum.pack_forget()
		self.errorExp.pack_forget()

#clg.debugLevel()
timestate = time.time()
filePath = "logs/{}.log".format(time.strftime("%Y%d%B_%H-%M-%S"), timestate)
with open(filePath, "a") as f:
	f.write("==================================================\nLog file.\n Date time : {}\n".format(time.strftime("%A %d %B %Y at %H:%M:%S"), timestate))
tk = tkinter.Tk()
dicplay = Display(tk)
tk.title("Power calculator")
tk.mainloop()
with open(filePath, "a") as f:
	f.write("[{time}] : Power off;\n==================================================\n".format(time = time.strftime("%A %d %B %Y at %H:%M:%S")))
