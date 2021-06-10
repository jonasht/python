import tkinter as tk
from tkinter import ttk

class MainProgram():
    def __init__(self):
        self.mainwin = tk.Tk()
        self.my_frame = FirstFrame()
        # examine the child parent relationship
        for child in self.mainwin.winfo_children():
            print(child['text'])
                

        
class FirstFrame():
    def __init__(self):
        self.firstframe = ttk.LabelFrame(text="hi")
        self.firstframe.grid(column=0, row=0)
        ttk.Label(master=self.firstframe,text='a widget inside frame').grid()

if __name__ == "__main__":
    main = MainProgram()
    main.mainwin.mainloop