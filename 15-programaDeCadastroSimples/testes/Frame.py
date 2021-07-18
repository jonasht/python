from tkinter import *
from tkinter.messagebox import showinfo


class MainFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        # options = {'padx': 5, 'pady': 5}

        # label
        self.label = Label(self, text='Hello, Tkinter!')
        self.label.grid()

        # button
        self.button = Button(self, text='Click Me', width=20)
        self.button['command'] = self.button_clicked
        self.button.grid(row=1, column=0, columnspan=YES)

        # show the frame on the container
        self.grid(row=0, column=2, padx=20)
        self.config(bg='red')

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')


class App(Tk):
    def __init__(self):
        super().__init__()
        # configucoes da janela root
        self.title('My Awesome App')
        self.geometry('400x500')
        self.bt1x = [True, False]
        self.bt2x = [True, False]
        self.bt3x = [True, False]
        Button(self, text='botao 1', width=10, command=self.bt1).grid(
            row=0, column=0, columnspan=1, sticky='NEWS')

        Button(self, text='botao 2', width=10, command=self.bt2).grid(
            row=1, column=0, columnspan=1, sticky='NEWS')
        
        Button(self, text='botao 3', width=10, command=self.bt3).grid(
            row=2, column=0, columnspan=1, sticky='NEWS')

        
    def bt1(self):
        
        if self.bt1x[0]:
            self.frame1 = MainFrame(self)
            self.frame1.config(bg='green')
            self.frame1.grid(row=0)
        else:
            self.frame1.grid_forget()
        self.bt1x.reverse()
        print(self.bt1x)
        
    def bt2(self):
        if self.bt2x[0]:
            self.frame2 = MainFrame(self)
            self.frame2.config(bg='blue')
            self.frame2.grid(row=1)
        else:
            self.frame2.grid_forget()

        self.bt2x.reverse()
        print(self.bt2x)
        
    def bt3(self):
        if self.bt3x[0]:
            self.frame3 = MainFrame(self)
            self.frame3.config(bg='pink')
            self.frame3.grid(row=2)
        else:
            self.frame3.grid_forget()
        self.bt3x.reverse()
        print(self.bt3x)

if __name__ == "__main__":
    app = App()

    app.mainloop()
