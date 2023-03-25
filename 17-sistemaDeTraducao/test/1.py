import translate 


def teste1(msg):
    s = translate.Translator(from_lang='pt-br',to_lang='en')

    res = s.translate(msg)
    
    
    

    print(res)

if __name__ == '__main__':
    teste1('oi tudo bem')




