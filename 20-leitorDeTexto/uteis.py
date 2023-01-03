import gtts



def get_dict_idioms() -> dict:
    lang = gtts.lang.tts_langs()


    
    
    # invertando 
    lang = dict(zip(lang.values(), lang.keys()))

    # colocando pt-br
    lang['portugues Brasil'] = 'pt-br'

    return lang


if __name__ == "__main__":
    
    langs = get_dict_idioms()
    print(langs.keys())
    print()
    print(list(langs.keys()))

    