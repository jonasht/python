print()

class loja:
    def __init__(self, notebook, mochila):
        self.notebook = notebook
        self.mochila = mochila
        
    def set_notebook(self, notebook):
        self.notebook = notebook

    def get_notebook(self):
        return self.notebook
    
    def set_mochila(self, mochila):
        self.mochila = mochila
        
    def get_mochila(self):
        return self.mochila
    

def enfeite(): print('=-'*30+'=')
# antigo preço
a = loja(notebook='137,00', mochila='3738,00')

enfeite()
print('preços antigos:')
print(f'notebook: {a.get_notebook()}')
print(f'mochila: {a.get_mochila()}')
enfeite()

guardar = a.get_notebook()
a.set_notebook(a.get_mochila())
a.set_mochila(guardar)


print(f'preços atualizados:\nnotebook:{a.get_notebook()} mochila:{a.get_mochila()}')
enfeite()
