from tkinter import *
from tkinter.messagebox import showinfo


class MainFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)

        # button
        self.button = Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')


class App(Tk):
    def __init__(self):
        super().__init__()
        # configucoes da janela root
        self.title('My Awesome App')
        self.geometry('300x100')


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()