import tkinter
from tkinter import Tk, ttk
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.grid()

lb = ttk.Label(app, text='isso soh eh um teste', color='green')

lb.grid()
txt = CTkTextbox(app)
txt.grid()

app.mainloop()