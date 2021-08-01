from tkinter import Tk, Frame, Button
from tkinter.constants import BOTTOM, TOP

    
app = Tk()

frame = Frame(app)

Button(frame, text='TOP').pack(side=TOP)
Button(frame, text='Botton').pack(side=BOTTOM)
frame.pack()

app.mainloop()


