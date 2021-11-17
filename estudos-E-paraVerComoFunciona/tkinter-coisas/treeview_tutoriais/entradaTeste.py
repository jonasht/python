from tkinter import ttk
import tkinter as tk


root = tk.Tk()

def atualizarLista(l):
    lb1.config(text=l)
    
def selecionador(event):
    letrasDigitadas = event.widget.get()
    print(letrasDigitadas)

    listaFiltrada = []

    if letrasDigitadas:
        for palavras in lista:
            if letrasDigitadas.lower() in palavras.lower():
                listaFiltrada.append(palavras)
        atualizarLista(listaFiltrada)
    else:
        atualizarLista(lista)
global lista
lista = ['jonas', 'lucas', 'alan', 'jorge', 'carol', 'fernando', 'Amanda',
         'Rafael', 'Igor', 'Vania', 'Vanilda', 'Vildenio', 'Fotus']


etd = ttk.Entry(root)
lb1 = ttk.Label(root, text='')
lb2 = ttk.Label(root, text=lista)

etd.pack()
lb1.pack()
lb2.pack()

etd.bind('<KeyRelease>', selecionador)


root.mainloop()