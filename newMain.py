#! /usr/bin/env python3
# coding: utf-8

import os
import tkinter as tk
import colorsLog as clg
import ast

def _loadSettings():
    with open("settings.cnf", "r") as f:
        return ast.literal_eval(f.read())

def _loadLanguages():
    languages = {}
    for i in settings.get("languages"):
        with open("languages/{}.lng".format(i), "r") as f:
            languages[i] = ast.literal_eval(f.read())
    return languages

settings = _loadSettings()
languages = _loadLanguages()
currentLanguage = languages.get(settings.get("currentLanguage"))


class MainWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.init()

    def init(self):
        self.top = {
            "titleFrame" : tk.Frame(self.window)
        }
        self.top["title"] = tk.Label(self.top.get("titleFrame"), text=currentLanguage.get("name"))
        self.top["settingsFrame"] = tk.Frame(self.top.get("titleFrame"))
        self.top["settingsButton"] = tk.Button(self.top.get("settingsFrame"), text=currentLanguage.get("settings"), command=self.displaySettings)

        self.home()

    def home(self):
        self.top.get("titleFrame").pack(side="top")
        self.top.get("settingsFrame").pack(side="right")
        self.top.get("settingsButton").pack()
        self.top.get("title").pack()


    def displaySettings(self):
        self.top.get("titleFrame").pack_forget()

def main():
    global settings, languages, currentLanguage
    mainWindow = MainWindow()
    mainWindow.window.mainloop()

if __name__ == "__main__":
    main()
    os.system("pause")
