import tkinter
import colorsLog as clg

def puissance(num, exposant = 2):
	out = 1
	if exposant > -1:
		for loop in range(exposant):
			clg.debug(out)
			out *= num
		return out
	elif exposant < 0:
		return 1 / puissance(num, -exposant)

class Display():
    def __init__(self, win):
        self.window = win
        self.titre = tkinter.Label(self.window, text = "Calculatrice de puissance").pack()
        self.enter = tkinter.Frame(self.window)
        self.numPuis = tkinter.Frame(self.enter)
        self.expLab = tkinter.Frame(self.enter)
        self.bottun = tkinter.Frame(self.window)

        self.labNum = tkinter.Label(self.numPuis, text = "Le nombre à mettre en puissance (a) : ")
        self.num = tkinter.StringVar()
        self.numEnt = tkinter.Entry(self.numPuis, textvariable = self.num, width = 30)
        self.labExp = tkinter.Label(self.expLab, text = "L'exposant (b) : ")
        self.exp = tkinter.StringVar()
        self.expEnt = tkinter.Entry(self.expLab, textvariable = self.exp, width = 30)
        self.go = tkinter.Button(self.bottun, text = "Calculer", command = self.calcul)
        self.res = tkinter.Button(self.bottun, text = "Reset", command = self.reset)
        self.result = tkinter.Label(self.window, text = "a puissance b = c")
        self.quitt = tkinter.Button(self.window, text = "Quitter", command = self.window.quit)
        self.errorNum = tkinter.Label(self.numPuis, text = "Veuillez entrer un nombre", fg = "red")
        self.errorExp = tkinter.Label(self.expLab, text = "Veuillez entrer un nombre entier", fg = "red")

        self.numPuis.pack(side = "top")
        self.expLab.pack(side = "bottom")
        self.enter.pack()
        self.bottun.pack()
        self.labNum.pack(side = "left")
        self.numEnt.pack(side = "right")
        self.labExp.pack(side = "left")
        self.expEnt.pack(side = "right")
        self.go.pack(side = "left")
        self.res.pack(side = "right")
        self.result.pack()
        self.quitt.pack()

    def calcul(self):
        try :
            	self.resu = puissance(float(self.num.get()), int(self.exp.get()))
        except ValueError :
                try :
                        float(self.num.get())
                except ValueError :
                        self.errorNum.pack(side = "left")
                else :
                        self.errorNum.pack_forget()
                try :
                        int(self.exp.get())
                except ValueError :
                        self.errorExp.pack(side = "left")
                else :
                        self.errorExp.pack_forget()
        else :
                self.errorNum.pack_forget()
                self.errorExp.pack_forget()
                self.result["text"] = "{} puissance {} = {}".format(self.num.get(), self.exp.get(), self.resu)

    def reset(self):
        self.result["text"] = "a puissance b = c"
        self.num.set("")
        self.exp.set("")
        self.errorNum.pack_forget()
        self.errorExp.pack_forget()

clg.debugLevel()
tk = tkinter.Tk()
dicplay = Display(tk)
tk.title("Calculatrice de puissance")
tk.mainloop()
