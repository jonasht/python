from tkinter import *        
from PIL import ImageTk, Image

app_root = Tk()

#Setting it up
# img = ImageTk.PhotoImage(Image.open("app.png"))
img = ImageTk.PhotoImage(Image.open("./img/home.jpg"))

#Displaying it
imglabel = Label(app_root, image=img).grid(row=1, column=1)        


app_root.mainloop()
