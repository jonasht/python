from tkinter import *
from cl_3x3 import *


class Frame_matriz(Frame):
    def __init__(self, parent, titulo, matriz, resposta = ''):
        super().__init__(parent)
        
        self.lb_titulo = Label(self, text=titulo, fg='blue').grid()
        self.frameMatriz = Frame(self)
        # colocando as labels
        for i, im in enumerate(matriz):
            for ii, iim in enumerate(im):
                Label(self.frameMatriz, text=f'{iim}').grid(row=i, column=ii, padx=5)
        self.frameMatriz.grid()
        self.lb_resposta = Label(self,text=resposta, fg='green').grid()

        
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
        
        # self.lb_matrizDelta = Label(self, text='')
        # self.lb_deltaResposta = Label(self, fg='green')

        
        # self.lb_deltaXResposta = Label(self, fg='green')
        # self.lb_deltaYResposta = Label(self, fg='green')
        # self.lb_deltaZResposta = Label(self, fg='green')
        
        self.lb_ContaRespostaX = Label(self, fg='green')
        self.lb_ContaRespostaY = Label(self, fg='green')
        self.lb_ContaRespostaZ = Label(self, fg='green')
        
        # self.lb_deltaResposta.pack()
        # self.lb_deltaXResposta.pack()
        # self.lb_deltaYResposta.pack()
        # self.lb_deltaZResposta.pack()
        
        # self.lb_ContaRespostaX.pack()
        # self.lb_ContaRespostaY.pack()
        # self.lb_ContaRespostaZ.pack()
        
        
        
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
 
        self.frame_matrizContas = Frame(self)
        self.matriz_delta = Frame_matriz( self.frame_matrizContas, 'matriz delta:', a.matriz_delta, (f'delta = {a.delta}'))
        self.matriz_deltaX = Frame_matriz(self.frame_matrizContas, 'matriz delta X:' ,a.matriz_deltaX, (f'delta x = {a.deltaX}'))
        self.matriz_deltaY = Frame_matriz(self.frame_matrizContas, 'matriz delta Y:',a.matriz_deltaY, (f'delta y = {a.deltaY}'))
        self.matriz_deltaZ = Frame_matriz(self.frame_matrizContas, 'matriz delta Z:', a.matriz_deltaZ, (f'delta z = {a.deltaZ}'))
        self.matriz_delta. grid(row=0, column=0, padx=5, pady=5)
        self.matriz_deltaX.grid(row=0, column=1, padx=5, pady=5)
        self.matriz_deltaY.grid(row=1, column=0, padx=5, pady=5)
        self.matriz_deltaZ.grid(row=1, column=1, padx=5, pady=5)
        self.frame_matrizContas.pack()


        self.lb_ContaRespostaX.config(text=f'x = {a.deltaX} / {a.delta} = {a.x}')
        self.lb_ContaRespostaY.config(text=f'y = {a.deltaY} / {a.delta} = {a.y}')
        self.lb_ContaRespostaZ.config(text=f'z = {a.deltaZ} / {a.delta} = {a.z}')
        self.lb_ContaRespostaX.pack()
        self.lb_ContaRespostaY.pack()
        self.lb_ContaRespostaZ.pack()
        
        
        self.lb_respostaX = Label(self, text=f'x = {a.x}')
        self.lb_respostaY = Label(self, text=f'y = {a.y}')
        self.lb_respostaZ = Label(self, text=f'z = {a.z}')
        self.lb_respostaX.pack()
        self.lb_respostaY.pack()
        self.lb_respostaZ.pack()

                
        

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x500')
    frame = Interface(root)
    frame.pack()
    root.mainloop()
        