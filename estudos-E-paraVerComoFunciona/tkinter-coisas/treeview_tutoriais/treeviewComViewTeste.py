from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *


ws = Tk()                       
ws.geometry("750x700")  


def show():
    etd.delete(0, END)     
    etd.focus()
    
    treeview.selection()
    conn = None
    try:
        conn = connect("data1.db")    
        cursor = conn.cursor()
        db = "select * from student"   
        cursor.execute(db)

        fetchdata = treeview.get_children()       
        for elements in fetchdata:
            treeview.delete(elements)
    

        data = cursor.fetchall()
        for d in data:
            treeview.insert("", END, values=d)

        conn.commit()
    except Exception as e:
        showerror("Fail", e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
    
def search():
    treeview.selection()


    fetchdata = treeview.get_children()
    print('fetchdata:', fetchdata)
    
    for f in fetchdata:
        treeview.delete(f)

    conn = None
    
    try:
        
        conn = connect("data1.db")
        core = conn.cursor()
        db = "select * from student where name = '%s' "
        name = etd.get()
        
        if (len(name) < 2) or (not name.isalpha()):
            pass
            showerror("fail", "invalid name")
        else:
            core.execute(db %(name))
            data = core.fetchall()
            for d in data:
                treeview.insert("", END, values=d)
            
    except Exception as e:
        showerror("issue", e)

    finally:
        if conn is not None:
            conn.close()
def reset():
    show()  

# testes
def mostrar():
    pass
def deletar():
    pass

scrollbarx = Scrollbar(ws, orient=HORIZONTAL)  
scrollbary = Scrollbar(ws, orient=VERTICAL)   
 
treeview = ttk.Treeview(ws, columns=("rollno", "name"), show='headings', height=22)  
treeview.pack()

treeview.heading('rollno', text="Roll No", anchor=CENTER)
treeview.column("rollno", stretch=NO, width = 100) 
treeview.heading('name', text="Name", anchor=CENTER)
treeview.column("name", stretch=NO)

scrollbary.config(command=treeview.yview)
scrollbarx.config(command=treeview.xview)
scrollbary.place(x = 526, y = 7)
scrollbarx.place(x = 220, y = 460)




ws_lbl = ttk.Label(ws, text = "Name", font=('calibri', 12, 'normal'))
ws_lbl.place(x = 290, y = 518)
etd = ttk.Entry(ws,  width = 20, font=('Arial', 15, 'bold'))
etd.place(x = 220, y = 540)
bt_pesquisar = Button(ws, text = 'Search',  width = 8, font=('calibri', 12, 'normal'), command = search)
bt_pesquisar.place(x = 480, y = 540)


show()      
ws.mainloop()
