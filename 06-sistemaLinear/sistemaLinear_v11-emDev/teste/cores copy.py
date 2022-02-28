from tkinter import *
from sys import exit

conta2x2 = 'x2y=5\n3x-5y=4'
root = Tk()
text = Text(root, width=20, height=10)
text.config(font='arial 20 bold')
text.insert(END, conta2x2)
text.pack()

def q_evento(event):
   exit()
root.bind('q', q_evento)

cs = conta2x2.split('\n')
print('cs', cs)
posicao = cs[0].find('y')
print('posicao:', posicao)

p1 = p2 = '1.'
p1 += str(posicao)
p2 += str(posicao+1)

print('p1:', p1, 'p2:', p2)


text.tag_add("y1", p1, p2)
text.tag_config("y1", background="black", foreground="green")

text.tag_config('1', foreground="green")
root.mainloop()