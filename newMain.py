#! /usr/bin/env python3
# coding: utf-8

import os
import tkinter as tk
import colorsLog as clg

def _loadSettings():
    pass

def _loadLanguages():
    pass

settings = _loadSettings()
global settings

class MainWindow(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.window = tk.Tk()

    def init(self):
        pass
