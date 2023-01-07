

# retornar as configuracoes de geometry p app ficar no meio da screen 
def get_configGeometry(parent, width:int=500, height:int=500) -> str:

    screen_x = parent.winfo_screenwidth()
    screen_y = parent.winfo_screenheight()

    screen_x = screen_x//2 - width//2
    screen_y = screen_y//2 - height//2
    
    return f'{width}x{height}+{screen_x}+{screen_y}'

    
    
if __name__ == "__main__":
    # teste
    print(get_configGeometry(500, 500))
