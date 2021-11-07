import tkinter as tk
from tkinter import ttk
from tkinter.constants import END

class Fr2(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller


        # self.tree = self.create_tree_widget()
        
        # self.columns = list()
        self.columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')

        # define headings
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')

        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        self.tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

        # insert a the end
        self.tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))

        # insert at the beginning
        self.tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))

        self.tree.insert('', END, values=('Jonas', 'Teixeira', 'Jonas.Teixeira@email.com.br'))
        
    def inserir(self, dados):
        nome = dados[0]
        sobrenome = dados[1]
        email = dados[2]
        # return tree
        self.tree.insert('', END, values=(nome, sobrenome, email))

    

if __name__ == '__main__':
    root = tk.Tk()
    fr = Fr2(root, root)
    fr.pack()
    root.mainloop()
    # from main import Principal
    