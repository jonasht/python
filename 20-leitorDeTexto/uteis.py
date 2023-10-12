import gtts



def get_dict_idioms() -> dict:
    lang = gtts.lang.tts_langs()

    # invertando 
    lang = dict(zip(lang.values(), lang.keys()))

    # colocando pt-br
    lang['portugues Brasil'] = 'pt-br'

    return lang
def write_theme(themeName=''):
    file_name='./config.txt'
    with open(file_name, 'w') as file:
        file.write(themeName)

def read_theme() -> str:
    file_name='./config.txt'
    with open(file_name, 'r') as file:
        return file.read()
    



if __name__ == "__main__":
    # print(theme_names)
    # print(list(lambda x: x.title(), theme_names))
    # print(list(map(lambda x: x.title(), theme_names)))
    print(read_theme())
    print(write_theme('darkly'))
    print(read_theme())
    