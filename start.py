#! /usr/bin/env python3
# coding: utf-8


"""
===== start.py =====

File to initialize the project.

"""


import os

settings = {
    "currentLanguage" : "english",
    "languages" : ["english", "francais"],
    "logs" : True
}

languages = {
    "english" : {
        "name" : "Power calculator",
        "settings" : "Settings",
        "languages" : "Change language",
        "logs" : ((True, "Enable logs"), (False, "Disable logs")),
        "calculate" : "Calculate (c)",
        "reset" : "Reset",
        "power" : "The power (b) : ",
        "number" : "The number to put in power (a) : ",
        "errorPower" : "The power must be a number (float or integer number)",
        "errorNumber" : "The number must be a number (float or integer number)",
        "quit" : "Quit"
    },
    "francais" : {
        "name" : "Calculatrice de puissance",
        "settings" : "Paramètres",
        "languages" : "Changer de langues",
        "logs" : ((True, "Logs activés"), (False, "Logs désactivés")),
        "calculate" : "Calculer (c)",
        "reset" : "Reset",
        "power" : "L'exposant (b) : ",
        "number" : "Le nombre à mettre en puissance (a) : ",
        "errorPower" : "L'exposant doit être un nombre (entier ou décimal)",
        "errorNumber" : "Le nombre à mettre en puissance doit être un nombre (entier ou décimal)",
        "quit" : "Quitter"
    }
}

try :
    os.mkdir("logs")     #Create the folder of logs.
except FileExistsError :     #If the floder is already created.
    pass

try:
    os.mkdir("languages")     #Create the languages' files' floder.
except FileExistsError :
    pass

with open("settings.cnf", "w") as f:
    f.write("{}".format(settings))

for language, value in languages.items():
    with open("languages/{}.lng".format(language), "w") as f:
        f.write("{}".format(value))
