from tkinter import *
import random
fontsize =30
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple', 'black', 'white']

def onSpan():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFlip)

def onGrow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, onGrow)

main = Tk()
mainLabel = Label(main, text='fun gui/Gui divertido',height=6, relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', height=5, command=onFlip).pack(fill=X)
Button(main, text='flip', height=5, command=onFlip).pack(fill=X)
Button(main, text='grow', height=5, command=onGrow).pack(fill=X)
main.mainloop()
