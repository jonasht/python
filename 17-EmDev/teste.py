import tkinter as tk

root = tk.Tk()
text = tk.Text(root,bg="white")
text.insert(tk.END,"This is a test message")
text.pack()
text.configure(font=("Times New Roman", 12, "bold"))
# root.wm_attributes("-transparentcolor", "white")
root.mainloop()