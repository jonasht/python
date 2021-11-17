
import tkinter as tk
from tkinter import Button, Entry, ttk
from tkinter.constants import NSEW, VERTICAL
from tkinter.messagebox import showinfo


class Fr1(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.lb_pesquisar = ttk.Label(self, text='pesquisar:')
        self.etd_pesquisar = ttk.Entry(self)
        self.bt_pesquisar = ttk.Button(self, text='pesquisar')
        self.lb_pesquisar.grid()
        self.etd_pesquisar.grid()
        self.bt_pesquisar.grid()
        
        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=0, column=0, sticky=NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
            print(record)
            self.controller.mostrar_dados(record)

if __name__ == '__main__':
    root = tk.Tk()
    frame = Fr(root)
    frame.pack()
    root.title('Treeview demo')
    root.geometry('620x200')

    root.mainloop()