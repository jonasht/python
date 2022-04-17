from tkinter import Tk, ttk
from tkinter.constants import CENTER, END, HORIZONTAL, VERTICAL, NO
from tkinter.messagebox import *
from sqlite3 import *


# conn = None

# conn = connect("data1.db")

  
# curs = conn.cursor()


# db = "create table student(rno int primary key, name text)"
# curs.execute(db)


# if conn is not None:
#     conn.close()    



# conn = None


# conn = connect("data1.db")


# curs = conn.cursor()


# db1 = "insert into student values(1,'Pauline')"
# db2 = "insert into student values(2,'Dexter')"
# db3 = "insert into student values(3,'Melba')"
# db4 = "insert into student values(4,'Roxanne')"
# db5 = "insert into student values(5,'Mary')"
# db6 = "insert into student values(6,'Andrew')"
# db7 = "insert into student values(7,'Renata')"


# curs.execute(db1)
# curs.execute(db2)
# curs.execute(db3)
# curs.execute(db4)
# curs.execute(db5)
# curs.execute(db6)
# curs.execute(db7)


# conn.commit()


# if conn is not None:
#     conn.close()

class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.scrollbarx = ttk.Scrollbar(self, orient=HORIZONTAL)  
        self.scrollbary = ttk.Scrollbar(self, orient=VERTICAL)    
        self.treeview = ttk.Treeview(self, columns=("rollno", "name"), show='headings', height=22)  
        self.treeview.pack()
        self.treeview.heading('rollno', text="Roll No", anchor=CENTER)
        self.treeview.column("rollno", stretch=NO, width = 100) 
        self.treeview.heading('name', text="Name", anchor=CENTER)
        self.treeview.column("name", stretch=NO)
        self.scrollbary.config(command=self.treeview.yview)
        self.scrollbary.place(x = 526, y = 7)
        self.scrollbarx.config(command=self.treeview.xview)
        self.scrollbarx.place(x = 220, y = 460)
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.map("Treeview")


        self.ws_lbl = ttk.Label(self, text = "Name")
        self.ws_lbl.place(x = 290, y = 518)
        self.ws_ent = ttk.Entry(self,  width = 20, font=('Arial', 15, 'bold'))
        self.ws_ent.place(x = 220, y = 540)
        
        self.ws_btn1 = ttk.Button(self, text = 'Search',  width = 8, command = self.search)
        self.ws_btn1.place(x = 480, y = 540)
        
        self.ws_btn2 = ttk.Button(self, text = 'Reset',  width = 8, command = self.reset)
        self.ws_btn2.place(x = 600, y = 540)


        self.show()  


    def show(self):
        self.ws_ent.delete(0, END)     
        self.ws_ent.focus()
        self.treeview.selection()
        conn = None
        try:
            conn = connect("data1.db")    
            cursor = conn.cursor()
            db = "select * from student"   
            cursor.execute(db)
            

            fetchdata = self.treeview.get_children()       
            for elements in fetchdata:
                self.treeview.delete(elements)
        

            data = cursor.fetchall()
            for d in data:
                self.treeview.insert("", END, values=d)

            conn.commit()
        except Exception as e:
            showerror("Fail", e)
            conn.rollback()
        finally:
            if conn is not None:
                conn.close()
                
    def search(self):
        self.treeview.selection()
        fetchdata = self.treeview.get_children()
        for f in fetchdata:
            self.treeview.delete(f)
        conn = None
        try:
            conn = connect("data1.db")
            core = conn.cursor()
            db = "select * from student where name = '%s' "
            name = self.ws_ent.get()
            if (len(name) < 2) or (not name.isalpha()):
                showerror("fail", "invalid name")
            else:
                core.execute(db %(name))
                data = core.fetchall()
                for d in data:
                    self.treeview.insert("", END, values=d)
                
        except Exception as e:
            showerror("issue", e)

        finally:
            if conn is not None:
                conn.close()
    def reset(self):
        self.show()  






if __name__ == '__main__':
    pass

    # ws = Tk()                       
    # ws.title("Python Guides")        
    # ws.geometry("750x700+400+50")  
    # ws.resizable(0, 0)            
    # view_window      

    # ws.mainloop()
    app = Tk()
    app.title('teste')
    frame = Fr(app)
    frame.pack()

    app.geometry("750x700+400+50")
    app.resizable(0, 0)
    app.mainloop()