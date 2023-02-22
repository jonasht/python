import tkinter as tk
from tkinter import ttk
 

 
 
 
class SeaofBTCapp(tk.Tk):
   def __init__(self,*args,**kwargs):
 
       tk.Tk.__init__(self,*args,**kwargs)
       tk.Tk.wm_title(self,"BTC")
       container = tk.Frame(self)
       container.pack(side="top",fill="both",expand=True)
       container.grid_rowconfigure(0,weight=1)
       container.grid_columnconfigure(0,weight=1)
       self.frames = {}
       for F in (StartPage,PageOne,PageTwo):
           frame = F(container,self)
           self.frames[F] = frame
           frame.grid(row=0,column=0,sticky="nsew")
       self.show_frame(StartPage)
 
   def show_frame(self,cont):
       frame = self.frames[cont]
       frame.tkraise()
 
 
 
class StartPage(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       label = tk.Label(self,text="Start Page")
       label.pack(padx=10,pady=10)
       button = ttk.Button(self,text="Visit Page 1",
                           command=lambda:controller.show_frame(PageOne))
       button.pack()
       button = ttk.Button(self, text="Visit Page 2",
                          command=lambda: controller.show_frame(PageTwo))
 
       button.pack()
 
 
class PageOne(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       label = tk.Label(self, text="Page One")
       label.pack(padx=10, pady=10)
       button = ttk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(StartPage))
 
       button.pack()
       button1 = ttk.Button(self, text="Page 2 ",
                          command=lambda: controller.show_frame(PageTwo))
 
       button1.pack()
 
 
class PageTwo(tk.Frame):
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       label = tk.Label(self, text="Page Two")
       label.pack(padx=10, pady=10)
       button = ttk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(StartPage))
 
       button.pack()
       button1 = ttk.Button(self, text="Go to Page1",
                          command=lambda: controller.show_frame(PageOne))
 
       button1.pack()
 
 
 
 
app = SeaofBTCapp()
app.mainloop()