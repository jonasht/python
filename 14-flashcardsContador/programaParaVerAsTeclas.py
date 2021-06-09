## Python 3.x
from tkinter import *



def key_in(event):
    ##shows key or tk code for the key
    if event.keysym == 'Escape':
        root.quit()
    if event.char == event.keysym:
        # normal number and letter characters
        label_str.set('Normal Key ' + event.char)
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        label_str.set('Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # everything else
        # F1 to F12, shift keys, caps lock, Home, End, Delete, Arrows ...
        label_str.set('Special Key %r' % (event.keysym))

root = Tk()
label_str= StringVar()
label_str.set(" ")
Label(root,textvariable=label_str, fg="blue").grid()
Label(root, text="Press a key (Escape key to exit\naperteTeclaESCape p Sair):" ).grid(row=1)

ent = Entry(root)
##ent.grid(row=0, column=1)   ##Not packed so will take any entry
ent.bind_all('<Key>', key_in)
ent.focus_set()

root.mainloop()
