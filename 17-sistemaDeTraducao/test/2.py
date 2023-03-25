import translate 

def def_trans(from_lang='pt-br', to_lang='en'):
    global trans 
    trans = translate.Translator(from_lang=from_lang,to_lang=to_lang)

def teste1(msg):
    global trans
    
    res = trans.translate(msg)
    
    
    

    print(res)

if __name__ == '__main__':
    def_trans()
    teste1('oi tudo bem')
    
    print()
    def_trans('en', 'es')
    teste1('hi, my name is jonas, what about you?')
    




