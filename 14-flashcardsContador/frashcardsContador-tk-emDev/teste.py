from tkinter import *
import tkinter
num = [i for i in range(10)]
print(num)

print(sum(num))
root = Tk()
Label(root, text=num, fg='lightgreen', bg='black').pack()
root.geometry('200x200')
root.mainloop()