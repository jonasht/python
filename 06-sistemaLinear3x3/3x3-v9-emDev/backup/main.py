from tkinter import *  
from cl_3x3 import *
from frameContas import *
        
class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # definindo frames 
        self.frame_principal = Frame(self)
        self.frameTOP = Frame(self.frame_principal, width=500)
        self.frameBAIXO = Frame(self.frame_principal)
        
        # botao fazer conta e botao conta default
        self.bt_contaDefault = Button(self.frameTOP, text='set conta default', command=self.mostrar_contaDefault)
        self.bt_contaDefault.pack(side=RIGHT)
        self.bt_sair = Button(self.frameTOP, text='Sair', command=self.quit)
        self.bt_sair.pack(side=LEFT, expand=True, fill=BOTH)
        
        self.bt_limpar = Button(self.frameBAIXO, text='Limpar', command=self.limparEntradas)
        self.bt_limpar.pack(side=LEFT)
        self.bt_fazerConta = Button(self.frameBAIXO, text='fazer conta', command=self.fazer_conta)
        self.bt_fazerConta.pack(side=RIGHT, expand=True, fill=BOTH)
        # declarando frame =======
        self.frame_conta = Frame(self.frame_principal)

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
        
    
        
        self.frameTOP.pack(fill=BOTH)
        self.frame_conta.pack()
        self.frameBAIXO.pack(fill=BOTH)
        
        self.frame_principal.pack()
        
        self.frame_todosResultados = Frame(self)
        
        
        
        bt_destruir = Button(self, text='destruir', command=self.destruir)
        bt_destruir.pack()
        
        self.mostrar_contaDefault()
        
    def destruir(self):
        print('destruir')
        self.frame_matrizContas.destroy()
        
        # self.matriz_delta.pack_forget()
        # self.matriz_deltaX.pack_forget()
        # self.matriz_deltaY.pack_forget()
        # self.matriz_deltaZ.pack_forget()
        
    def mostrar_contaDefault(self):
        
        # desativando botao
        self.bt_contaDefault.config(state=DISABLED)
        
        conta = [
        {'x': 1, 'y': 2, 'z': 1, '=': 8},
        {'x': 2, 'y': -1, 'z': 1, '=': 3},
        {'x': 3, 'y': 1, 'z': -1, '=': 2}
        ]
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
    
    # limpar todas as entradas/Entry ===================
    def limparEntradas(self):
        self.etd_x1.delete(0, END)
        self.etd_y1.delete(0, END)
        self.etd_z1.delete(0, END)
        self.etd_x2.delete(0, END)
        self.etd_y2.delete(0, END)
        self.etd_z2.delete(0, END)
        self.etd_x3.delete(0, END)
        self.etd_y3.delete(0, END)
        self.etd_z3.delete(0, END)
        
        self.etd_igual1.delete(0, END)
        self.etd_igual2.delete(0, END)
        self.etd_igual3.delete(0, END)
        
    # pega os numeros de entradas/Entry
    def get_numDeEntradas(self):
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
        return conta
    
    def fazer_conta(self):
        # self.bt_fazerConta.config(state=DISABLED)
        
        conta = self.get_numDeEntradas()
        a = cl_3x3(conta)
 
        self.frame_matrizContas = Frame(self.frame_todosResultados)
        self.matriz_delta = Frame_matriz( self.frame_matrizContas, 'matriz delta:', a.matriz_delta, (f'delta = {a.delta}'))
        self.matriz_deltaX = Frame_matriz(self.frame_matrizContas, 'matriz delta X:' ,a.matriz_deltaX, (f'delta x = {a.deltaX}'))
        self.matriz_deltaY = Frame_matriz(self.frame_matrizContas, 'matriz delta Y:',a.matriz_deltaY, (f'delta y = {a.deltaY}'))
        self.matriz_deltaZ = Frame_matriz(self.frame_matrizContas, 'matriz delta Z:', a.matriz_deltaZ, (f'delta z = {a.deltaZ}'))
        self.matriz_delta. grid(row=0, column=0, padx=5, pady=5)
        self.matriz_deltaX.grid(row=0, column=1, padx=5, pady=5)
        self.matriz_deltaY.grid(row=1, column=0, padx=5, pady=5)
        self.matriz_deltaZ.grid(row=1, column=1, padx=5, pady=5)
        self.frame_matrizContas.pack()

        self.frame_resultadoFinal1 = Frame(self.frame_todosResultados)
        self.frame_resultadoFinal2 = Frame(self.frame_todosResultados)

        self.lb_ContaRespostaX = Label(self.frame_resultadoFinal1, 
                                       fg='green', 
                                       text=f'x = {a.deltaX} / {a.delta} = {a.x}')
        self.lb_ContaRespostaY = Label(self.frame_resultadoFinal1, fg='green',
                                       text=f'y = {a.deltaY} / {a.delta} = {a.y}')
        self.lb_ContaRespostaZ = Label(self.frame_resultadoFinal1, 
                                       fg='green',
                                       text=f'z = {a.deltaZ} / {a.delta} = {a.z}')
        self.lb_ContaRespostaX.pack()
        self.lb_ContaRespostaY.pack()
        self.lb_ContaRespostaZ.pack()
        
        self.lb_respostaX = Label(self.frame_resultadoFinal2, text=f'x = {a.x}', font='bold')
        self.lb_respostaY = Label(self.frame_resultadoFinal2, text=f'y = {a.y}', font='bold')
        self.lb_respostaZ = Label(self.frame_resultadoFinal2, text=f'z = {a.z}', font='bold')
        self.lb_respostaX.pack()
        self.lb_respostaY.pack()
        self.lb_respostaZ.pack()

        self.frame_resultadoFinal1.pack(side=LEFT)
        self.frame_resultadoFinal2.pack(side=RIGHT)
        self.frame_todosResultados.pack()
        
        

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x500')
    frame = Interface(root)
    frame.pack()
    root.mainloop()
        