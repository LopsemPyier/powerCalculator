#! /usr/bin/env/ python3
# coding: utf-8


"""
===== start.py =====

File to initialize the project.

"""


import os


try :
    os.mkdir("logs")     #Create the folder of logs.
except FileExistsError :
    pass
