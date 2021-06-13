from enum import IntEnum
from tkinter import *
from cl_3x3 import *

class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        
        # declarando frame =======
        self.frame_conta = Frame(self)

        # 1 ============== conta
        self.etd_x1 = Entry(self.frame_conta, width=5)
        self.lb_x1 = Label(self.frame_conta, text='X')
        
        self.etd_y1 = Entry(self.frame_conta, width=5)
        self.lb_y1 = Label(self.frame_conta, text='Y')
        
        self.etd_z1 = Entry(self.frame_conta, width=5)
        self.lb_z1 = Label(self.frame_conta, text='Z')

        # 2 ============== conta
        self.etd_x2 = Entry(self.frame_conta, width=5)
        self.lb_x2 = Label(self.frame_conta, text='X')

        self.etd_y2 = Entry(self.frame_conta, width=5)
        self.lb_y2 = Label(self.frame_conta, text='Y')

        self.etd_z2 = Entry(self.frame_conta, width=5)
        self.lb_z2 = Label(self.frame_conta, text='Z')

        # 3 conta =============
        self.etd_x3 = Entry(self.frame_conta, width=5)
        self.lb_x3 = Label(self.frame_conta, text='X')

        self.etd_y3 = Entry(self.frame_conta, width=5)
        self.lb_y3 = Label(self.frame_conta, text='Y')
        
        self.etd_z3 = Entry(self.frame_conta, width=5)
        self.lb_z3  = Label(self.frame_conta, text='Z')
        
        # sinal  (=) de igual =====================

        self.etd_igual1 = Entry(self.frame_conta, width=5)
        self.lb_igual1 = Label(self.frame_conta, text='=')
        
        self.etd_igual2 = Entry(self.frame_conta, width=5)
        self.lb_igual2 = Label(self.frame_conta, text='=')

        self.etd_igual3 = Entry(self.frame_conta, width=5)
        self.lb_igual3 = Label(self.frame_conta,text='=')
        
        
        # colocando frame conta na tela ==========
        self.etd_x1.grid(row=1, column=1)
        self.lb_x1.grid(row=1, column=2)
        self.etd_y1.grid(row=1, column=3)
        self.lb_y1.grid(row=1, column=4)
        self.etd_z1.grid(row=1, column=5)
        self.lb_z1.grid(row=1, column=6)
        
        self.etd_x2.grid(row=2, column=1)
        self.lb_x2.grid(row=2, column=2)
        self.etd_y2.grid(row=2, column=3)
        self.lb_y2.grid(row=2, column=4)
        self.etd_z2.grid(row=2, column=5)
        self.lb_z2.grid(row=2, column=6)
        
        self.etd_x3.grid(row=3, column=1)
        self.lb_x3.grid(row=3, column=2)
        self.etd_y3.grid(row=3, column=3)
        self.lb_y3.grid(row=3, column=4)
        self.etd_z3.grid(row=3, column=5)
        self.lb_z3.grid(row=3, column=6)
        
        self.etd_igual1.grid(row=1, column=8)
        self.lb_igual1.grid(row=1, column=7)
        self.etd_igual2.grid(row=2, column=8)
        self.lb_igual2.grid(row=2, column=7)
        self.etd_igual3.grid(row=3, column=8)
        self.lb_igual3.grid(row=3, column=7)
        
        self.frame_conta.pack()
        
        # botao fazer conta e botao conta default 
        self.bt_fazerConta = Button(self, text='fazer conta', command=self.fazer_conta)
        self.bt_contaDefault = Button(self, text='set conta default', command=self.mostrar_contaDefault)

        self.bt_fazerConta.pack()
        self.bt_contaDefault.pack()
        
        self.lb_matrizDelta = Label(self, text='')
        self.lb_deltaResposta = Label(self, fg='green')

        self.lb_matrizDeltaX = Label(self)
        self.lb_deltaXResposta = Label(self, fg='green')

        self.lb_matrizDeltay = Label(self)
        self.lb_deltaYResposta = Label(self, fg='green')

        self.lb_matrizDeltaz = Label(self)
        self.lb_deltaZResposta = Label(self, fg='green')
        
        self.lb_respostaX = Label(self, fg='green')
        self.lb_respostaY = Label(self, fg='green')
        self.lb_respostaZ = Label(self, fg='green')
        
        self.lb_matrizDelta.pack()
        self.lb_deltaResposta.pack()
        self.lb_matrizDeltaX.pack()
        self.lb_deltaXResposta.pack()
        self.lb_matrizDeltay.pack()
        self.lb_deltaYResposta.pack()
        self.lb_matrizDeltaz.pack()
        self.lb_deltaZResposta.pack()
        
        self.lb_respostaX.pack()
        self.lb_respostaY.pack()
        self.lb_respostaZ.pack()
        
        
        
        self.mostrar_contaDefault()
    def mostrar_contaDefault(self):
        # desativando botao
        self.bt_contaDefault.config(state=DISABLED)
        
        conta = [
        {'x': 1, 'y': 2, 'z': 1, '=': 8},
        {'x': 2, 'y': -1, 'z': 1, '=': 3},
        {'x': 3, 'y': 1, 'z': -1, '=': 2}
        ]
        # self.etd_x1.config(textvariable=1)
        self.etd_x1.insert(0, conta[0]['x'])
        self.etd_y1.insert(0, conta[0]['y'])
        self.etd_z1.insert(0, conta[0]['z'])
        self.etd_x2.insert(0, conta[1]['x'])
        self.etd_y2.insert(0, conta[1]['y'])
        self.etd_z2.insert(0, conta[1]['z'])
        self.etd_x3.insert(0, conta[2]['x'])
        self.etd_y3.insert(0, conta[2]['y'])
        self.etd_z3.insert(0, conta[2]['z'])
        
        self.etd_igual1.insert(0, conta[0]['='])
        self.etd_igual2.insert(0, conta[1]['='])
        self.etd_igual3.insert(0, conta[2]['='])
    
    def fazer_conta(self):
        x1 = int(self.etd_x1.get())
        x2 = int(self.etd_x2.get())
        x3 = int(self.etd_x3.get())
        y1 = int(self.etd_y1.get())
        y2 = int(self.etd_y2.get())
        y3 = int(self.etd_y3.get())
        z1 = int(self.etd_z1.get())
        z2 = int(self.etd_z2.get())
        z3 = int(self.etd_z3.get())
        igual1 = int(self.etd_igual1.get())
        igual2 = int(self.etd_igual2.get())
        igual3 = int(self.etd_igual3.get())
        
        conta = [
                {'x': x1, 'y': y1, 'z': z1, '=': igual1},
                {'x': x2, 'y': y2, 'z': z2, '=': igual2},
                {'x': x3, 'y': y3, 'z': z3, '=': igual3}
        ]
        a = cl_3x3(conta)

        print('conta:')
        a.mostrar_conta()
        
        # 
        print('matriz delta:')
        a.mostrar_matriz()
        print(f'delta = {a.delta}')
        self.lb_matrizDelta.config(text=f'{a.matriz_delta[0]}\n{a.matriz_delta[1]}\n{a.matriz_delta[2]}')
        self.lb_deltaResposta.config(text=f'delta = {a.delta}')
        
        # a.mostrar_matriz('x')
        # print(f'deltaX = {a.deltaX}')
        self.lb_matrizDeltaX.config(text=f'{a.matriz_deltaX[0]}\n{a.matriz_deltaX[1]}\n{a.matriz_deltaX[2]}')
        self.lb_deltaXResposta.config(text=f'delta X = {a.deltaX}')

        # a.mostrar_matriz('y')
        # print(f'deltaX = {a.deltaY}')
        self.lb_matrizDeltay.config(text=f'{a.matriz_deltaY[0]}\n{a.matriz_deltaY[1]}\n{a.matriz_deltaY[2]}')
        self.lb_deltaYResposta.config(text=f'delta Y = {a.deltaY}')

        # a.mostrar_matriz('z')
        # print(f'deltaZ = {a.deltaZ}')
        self.lb_matrizDeltaz.config(text=f'{a.matriz_deltaZ[0]}\n{a.matriz_deltaZ[1]}\n{a.matriz_deltaZ[2]}')
        self.lb_deltaZResposta.config(text=f'delta Z = {a.deltaZ}')
        # print(f'delta={a.delta}, deltaX={a.deltaX}, deltaY={a.deltaY}, deltaZ={a.deltaZ}')

        # print(f'x = {a.deltaX}/{a.delta} = {a.x}\n')
        # print(f'y = {a.deltaY}/{a.delta} = {a.y}\n')
        # print(f'z = {a.deltaZ}/{a.delta} = {a.z}\n')
        
        self.lb_respostaX.config(text=f'x = {a.deltaX}/{a.delta} = {a.x}')
        self.lb_respostaY.config(text=f'y = {a.deltaY}/{a.delta} = {a.y}')
        self.lb_respostaZ.config(text=f'z = {a.deltaZ}/{a.delta} = {a.z}')
        
        # print(f'x = {a.x}, y = {a.y}, z = {a.z}')

                
        

if __name__ == '__main__':
    root = Tk()
    frame = Interface(root)
    frame.pack()
    root.mainloop()
        
# --------------------------------------------------
# conta = [
#     {'x': 1, 'y': 2, 'z': 1, '=': 8},
#     {'x': 2, 'y': -1, 'z': 1, '=': 3},
#     {'x': 3, 'y': 1, 'z': -1, '=': 2}
# ]
# --------------------------------------------------

# a = cl_3x3(conta)

print()


# print('conta:')
# a.mostrar_conta()

# print('matriz delta:')
# a.mostrar_matriz()
# print(f'delta = {a.delta}')


# a.mostrar_matriz('x')
# print(f'deltaX = {a.deltaX}')

# a.mostrar_matriz('y')
# print(f'deltaX = {a.deltaY}')

# a.mostrar_matriz('z')

# print(f'deltaZ = {a.deltaZ}')

# print(f'delta={a.delta}, deltaX={a.deltaX}, deltaY={a.deltaY}, deltaZ={a.deltaZ}')

# print(f'x = {a.deltaX}/{a.delta} = {a.x}\n')
# print(f'y = {a.deltaY}/{a.delta} = {a.y}\n')
# print(f'z = {a.deltaZ}/{a.delta} = {a.z}\n')

# print(f'x = {a.x}, y = {a.y}, z = {a.z}')
