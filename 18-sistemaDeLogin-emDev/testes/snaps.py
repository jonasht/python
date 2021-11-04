from tkinter import ttk


from tkinter import *

class app(Tk):
    def __init__(self, screenName: str | None = ..., baseName: str | None = ..., className: str = ..., useTk: bool = ..., sync: bool = ..., use: str | None = ...) -> None:
        super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
        
        self.lb = Label(self, text = 'so um teste')
        self.lb.grid(row = 0, column = 0)
        

