import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

window = ttk.Window()


window.geometry('600x400')



window.bind('q', lambda x: window.quit())
window.bind('<Escape>', lambda x: window.quit())
lb_teste = ttk.Label(window, text='isso so ẽ um teste')
lb_teste.pack()
bt = ttk.Button(window, style=LINK, padding=0)
image = Image.open('./contexto.png')
image = image.resize((100, 100), Image.LANCZOS)
photo_img = ImageTk.PhotoImage(image)
bt.config(image=photo_img)
bt.pack()

print(window.style.theme_names())
window.place_window_center()
window.style.theme_use('cyborg')
window.mainloop()


