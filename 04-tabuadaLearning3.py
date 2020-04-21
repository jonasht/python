from tkinter import *
import random
t = Tk()
t.title('FTabuada v3')
t.iconbitmap('04/ico.xbm')
conta_1 = 2
conta_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(conta_2)
c = 0
incorreto = correto = 0


def Start():
    conta_1 = valor.get()
    conta_total = [conta_1 * conta_2[0], (conta_1 * conta_2[0]) + 2, (conta_1 * conta_2[c]) * 1  ]
    random.shuffle(conta_total)
    lb_conta.config(text=str(conta_1) + ' X ' + str(conta_2[0]))
    bt0.config(text=conta_total[0], state=NORMAL)
    bt1.config(text=conta_total[1], state=NORMAL)
    bt2.config(text=conta_total[2], state=NORMAL)
    
    bt_start.config(state=DISABLED, fg='white', bg='white')
    
    
def comando(res_comando):
    global conta_total
    global conta_1
    global conta_2
    global c
    global correto
    global incorreto
    conta_1 = valor.get()
    
    if c <= len(conta_2):
        c = c + 1
    
    
    conta_total = [conta_1 * conta_2[c], (conta_1 * conta_2[c]) + 7,(conta_1 * conta_2[c]) * 2 + 9 ]
    
    lb_conta.config(text=str(conta_1) + ' X ' + str(conta_2[c]))
    
    lb_conta_resposta.config(text=str(conta_1) + ' X ' + str(conta_2[c-1]) + ' = ' + str(conta_1 * conta_2[c-1]))
    
    bt0.config(text=conta_total[0], state=NORMAL)
    bt1.config(text=conta_total[1], state=NORMAL)
    bt2.config(text=conta_total[2], state=NORMAL)
    
    if (conta_1 * conta_2[c]) == conta_total[res_comando]:
        lb_resposta.config(text='correto')
        correto = correto + 1
        lb_correto.config(text=correto)
        random.shuffle(conta_total)
    else:
        lb_resposta.config(text='incorreto')
        incorreto = incorreto + 1
        lb_incorreto.config(text=incorreto)
        random.shuffle(conta_total)



lb_conta = Label(t, text='=-=-=-=', width=5, fg='red', font='arial 80 bold')

lb_resposta = Label(t, text='=-=-=-=-=-=', fg='blue', font='arial 20 bold')
lb_conta_resposta = Label(t, text='=-=-=-=-=-=', fg='dark blue', font='arial 20 bold')
bt0 = Button(t, text='', command=lambda: comando(0), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)
bt1 = Button(t, text='', command=lambda: comando(1), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)
bt2 = Button(t, text='', command=lambda: comando(2), state=DISABLED, font='arial 20 bold', 
             width=5, borderwidth=2)

bt_start = Button(t, text='start', command=Start, font='arial 20')

frame_op = Frame(t)
frame_op.grid(row=0, column=0, columnspan=3, sticky=W+E)

valor = IntVar()

lb_op = Label(frame_op, text='qual tabuada?:')
lb_op.grid(row=0)

rbt1 = Radiobutton(frame_op, text='1', variable=valor, value=1, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt1.grid(row=0, column=1)
rbt2 = Radiobutton(frame_op, text='2', variable=valor, value=2, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt2.grid(row=0, column=2)
rbt3 = Radiobutton(frame_op, text='3', variable=valor, value=3, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt3.grid(row=0, column=3)
rbt4 = Radiobutton(frame_op, text='4', variable=valor, value=4, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt4.grid(row=0, column=4)
rbt5 = Radiobutton(frame_op, text='5', variable=valor, value=5, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt5.grid(row=0, column=5)

rbt6 = Radiobutton(frame_op, text='6', variable=valor, value=6, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt6.grid(row=0, column=6)
rbt7 = Radiobutton(frame_op, text='7', variable=valor, value=7, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt7.grid(row=0, column=7)
rbt8 = Radiobutton(frame_op, text='8', variable=valor, value=8, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt8.grid(row=0, column=8)
rbt9 = Radiobutton(frame_op, text='9', variable=valor, value=9, indicatoron=0, padx=10, pady=10,
                   bg='green')
rbt9.grid(row=0, column=9)
rbt10 = Radiobutton(frame_op, text='10', variable=valor, value=10, indicatoron=0,
                     padx=10, pady=10, bg='green')
rbt10.grid(row=0, column=10)

rbt9.select()

lb_conta.grid(row=1, columnspan=3, sticky=W+E)
lb_resposta.grid(row=2, column=1,columnspan=2, sticky=W+E)
lb_conta_resposta.grid(row=3, column=1, columnspan=2, sticky=W+E)


bt0.grid(row=2, sticky=W+E)
bt1.grid(row=3, sticky=W+E)
bt2.grid(row=4, sticky=W+E)
bt_start.grid(row=5, columnspan=3, sticky=W+E)

lb_correto = Label(t, text=0, fg='blue', font='arial 20 bold')
lb_incorreto = Label(t, text=0, fg='red', font='arial 20 bold')

lb_incorreto.grid(row=4, column=1)
lb_correto.grid(row=4, column=2)


t.mainloop()