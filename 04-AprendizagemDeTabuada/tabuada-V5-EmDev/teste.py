from tkinter import Button, Frame, Tk    

class classeBotao:
    def __init__(self, master):
       frame = Frame(master)
       frame.pack()
       master.geometry('400x400')
       self.button = Button(frame, text="Hello", command=self.func1)
       self.button.pack(side='left')

       master.bind('1', self.func1)
       master.bind('2', self.func2)
       master.bind('3', self.func3)

    def func1(self, _event=None):
        print('o 1 foi apertado')
    def func2(self, _event=None):
        print('o 2 foi apertado')
    def func3(self, _event=None):
        print('o 3 foi apertado')

if __name__ == '__main__':
    root = Tk()
    abc = classeBotao(root)
    root.mainloop()
