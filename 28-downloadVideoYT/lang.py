



class Languages:
    def __init__(self) -> None:
        self.pt = dict(bt_1='botao um',
                       lb_1='label um',
                       lb_2='label dois')

                       
        self.en = dict(lb_title='Paste the Links for Downloading',
                       bt_delete='Delete',
                       lb_lang='Language:',
                       bt_paste='Paste',
                       bt_download='Download',
                       lb_msg='Esc to Exit',
                       lb_file='file:',
                       bt_file='Open file',
                       lb_theme='Theme:',
                       toplevel_title='config',
                       bt_toplevelQuit='Quit')

        
        self.languages = ['portuguese', 'english']
        
        self.set_lang('en')
        

    @property
    def lb_title(self):
        return self.lang_dict['lb_title']
    @property        
    def bt_delete(self):
        return self.lang_dict['bt_delete']
    @property        
    def lb_lang(self):
        return self.lang_dict['lb_lang']
    @property        
    def bt_paste(self):
        return self.lang_dict['bt_paste']
    @property        
    def bt_download(self):
        return self.lang_dict['bt_download']
    @property        
    def lb_msg(self):
        return self.lang_dict['lb_msg']
    @property        
    def lb_file(self):
        return self.lang_dict['lb_file']
    @property        
    def bt_file(self):
            return self.lang_dict['bt_file'] 
    @property            
    def lb_theme(self):
        return self.lang_dict['lb_theme']

    @property    
    def toplevel_title(self):
        return self.lang_dict['toplevel_title']

    @property    
    def bt_toplevelQuit(self):
        return self.lang_dict['bt_toplevelQuit']

    def set_lang(self, lang):
        if lang == 'en':
            self.lang_dict = self.en.copy()
            self.language = 'en'
        elif lang == 'pt':
            self.lang_dict = self.pt.copy()
            self.language = 'pt'

if __name__ == '__main__':
    l = Languages()
    # print(l.pt)
    
    print('language:', l.language)
    print('lb_title:', l.lb_title)
    print('bt_delete:', l.bt_delete)
    print('lb_lang:', l.lb_lang)
    print('bt_paste:', l.bt_paste)
    print('bt_download:', l.bt_download)
    print('lb_msg:', l.lb_msg)
    print('lb_file:', l.lb_file)
    print('bt_file:', l.bt_file)
    print('lb_theme:', l.lb_theme)
    print('toplevel_title:', l.toplevel_title)
    print('bt_toplevelQuit:', l.bt_toplevelQuit)