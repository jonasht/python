from tkinter import *

class classeBotao(Tk):
    def __init__(self):
       super().__init__()
       
       frame = Frame(self)
       frame.pack()
       self.geometry('400x400')
       self.button = Button(frame, text="Hello", command=self.func1)
       self.button.pack(side='left')

       self.bind('1', self.func1)
       self.bind('2', self.func2)
       self.bind('3', self.func3)

    def func1(self, event):
        print('o 1 foi apertado')
    def func2(self, _event=None):
        print('o 2 foi apertado')
    def func3(self, _event=None):
        print('o 3 foi apertado')

if __name__ == '__main__':
    
    root = classeBotao()
    root.mainloop()
