from tkinter import *

def onclick():
   pass
t= '''algo eu
algo algo 
 estou escrevendo algo
eu estou escrevendo algo 
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo
eu estou escrevendo algo 
eu estou escrevendo algo
eu estou escrevendo algo

'''
root = Tk()
text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
text.insert(END, t)
text.pack()

text.tag_add("algo", "1.0", "1.4")
# text.tag_add("algo", END)
text.tag_add("1", "1.8", "2.13")
text.tag_config("algo", background="yellow", foreground="blue")
text.tag_config("1", background="black", foreground="green")
root.mainloop()