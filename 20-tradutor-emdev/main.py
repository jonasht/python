from tkinter import Button, Tk, Text, ttk
from tkinter.constants import BOTH, BOTTOM, EW, RIGHT, TOP, LEFT, YES
from googletrans import Translator

def traduzir():
    texto = ''
    src = ''
    dest = ''
    resultado = ''

    translator = Translator()
    resultado = translator.translate('oi pessoa', src='pt', dest='en')

    print(resultado.text)
    return resultado.text


janela = Tk()
janela.title('Tradutor')

values = ('pt', 'es', 'en')

fr_meio = ttk.Frame()
fr_esquerdo = ttk.Frame(fr_meio)
fr_direito = ttk.Frame(fr_meio)


lb_entrada = ttk.Label(fr_esquerdo, text='Entrada')
combo_entrada = ttk.Combobox(fr_esquerdo, values=values)
txt1 = Text(fr_esquerdo)

lb_saida = ttk.Label(fr_direito, text='Saida')
combo_saida = ttk.Combobox(fr_direito, values=values)
txt2 = Text(fr_direito)

# botao traduzir 
bt_translate = ttk.Button(text='traduzir')
# default
combo_entrada.set('pt')
combo_saida.set('en')

lb_entrada.grid()
combo_entrada.grid()
txt1.grid()

lb_saida.grid()
combo_saida.grid()
txt2.grid()

fr_esquerdo.pack(side=LEFT, fill=BOTH, expand=YES)
fr_direito.pack(side=RIGHT, fill=BOTH, expand=YES)
fr_meio.pack()
bt_translate.pack(fill=BOTH, expand=YES )


janela.mainloop()