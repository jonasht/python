
from tkinter import *
from tkinter import ttk
from colorama.ansi import Fore 

cores = [
    Fore.BLUE,
    Fore.GREEN,
    Fore.RED,
    Fore.YELLOW,
    Fore.WHITE, 
    Fore.CYAN,
    Fore.LIGHTMAGENTA_EX
]
def colorir(word):
    w_return = ''
    for c, w in zip(cores, word):
        w_return += c+w
    print(w_return)
    return w_return

teste = colorir('teste')
root = Tk()
root.geometry('500x500')
lb = ttk.Label(root, text=teste)
lb.pack()
lb2 = Label(root, text=teste)
lb2.pack()

root.mainloop()
# it doesnt work