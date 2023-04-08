import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import utils as u



class Window(ttk.Window):
    def __init__(self) -> None:
        super().__init__()
        
        self.text = ttk.Text(self)
        self.bt_putTag = ttk.Button(self, text='put tag', command=self.cmd_tag)

        self.bt_putTag.pack()

        self.text.pack()

        self.text.insert(1.0, u.read(path='links.txt'))
    def cmd_tag(self):
        error_lines = [
            True,
            True,
            True,
            True,
            True,
            True,False, False
        ]
        lines = self.text.get(1.0, END)
        lines = lines.split('\n')
        while '' in lines: lines.remove('')
        print(lines)
        lines_names = list()
        # criando tag names
        for i, line in enumerate(lines):
            self.text.tag_add(f'l{i+1}', f'{i+1}.0', f'{i+1}.{len(line)}') 
            print(f'l{i+1}', f'{i+1}.0', f'{i+1}.{len(line)}') 
            lines_names.append(f'l{i+1}')
            
        print('lines name', lines_names)
        # self.text.tag_add('l1', 1.0, 1.6)        
        for name, error in zip(lines_names, error_lines):
            if error:
                
                self.text.tag_config(name, foreground='green')
            else:
                self.text.tag_config(name, foreground='red')
                
        
        
        
window = Window()

window.style.theme_use('cyborg')
window.bind('q', lambda x: window.quit())
window.geometry('500x500')




window.mainloop()