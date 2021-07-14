import tkinter as tk
 
 
class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.create_start_frame()
 
    def create_start_frame(self):
        self.start_frame = StartFrame(self.root)
        self.start_frame.btn_start.bind(
            '<Button-1>', self.on_start_frame_btn_start)
        self.start_frame.pack()
 
    def on_start_frame_btn_start(self, event):
        self.start_frame.destroy()
        self.second_menu_frame = SecondMenuFrame(root)
        self.second_menu_frame.btn_option1.bind(
            '<Button-1>', self.on_second_menu_frame_btn_option1)
        self.second_menu_frame.pack()
 
    def on_second_menu_frame_btn_option1(self, event):
        self.second_menu_frame.destroy()
        self.final_frame = FinalFrame(root)
        self.final_frame.pack()
 
 
class StartFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='StartFrame').pack()
        self.btn_start = tk.Button(
            self, text="Press here to start", bg="red", fg="black", font="Helvitica 30")
        self.btn_start.pack()
 
 
class SecondMenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='SecondMenuFrame').pack()
        self.btn_option1 = tk.Button(self, text="Option1", bg="white",
                                     fg="firebrick", relief="groove", font="Helvitica 30")
        self.btn_option1.pack()
 
 
class FinalFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='FinalFrame').pack()
        self.btn_final1 = tk.Button(self, text="finalsel1", bg="white",
                                    fg="firebrick", relief="groove", font="Helvitica 30", )
        self.btn_final1.pack()
 
print(issubclass(FinalFrame, Main))
 
if __name__ == "__main__":
    root = tk.Tk()
 
    main = Main(root)
    root.mainloop()