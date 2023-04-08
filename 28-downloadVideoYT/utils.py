

def read(path):
    with open(path, 'r') as reader:
        text = reader.read()
        return text


def write(path, text):
    with open(path, 'w') as writer:
        writer.write(text)


def get_configTheme():
    return read('./config.txt')

def set_configTheme(theme):
    write('./config.txt', theme)


if __name__ == "__main__":
    # write('text.txt', 'hello world')

    # print(read('./text.txt'))
    set_configTheme('cyborg')
    print(get_configTheme())
    
    import ttkbootstrap as ttk
    
    w = ttk.Window()
    themes = w.style.theme_names()
    print(themes)
    
    print(themes.index('lumen'))
    w.style.theme_use(get_configTheme())
    print(w.style.theme_use())