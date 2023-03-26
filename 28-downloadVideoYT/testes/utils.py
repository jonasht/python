

def read(path:str) -> str:
    with open(path, 'r') as file:
        return file.read()

def write(path, txt:str) -> None:
    with open(path, 'w') as file:
        file.write(txt)

        

        
        
# teste 
def __teste_read():
    print('teste read')
    
    txt = read('./filedialog3.py')
    print(f'type:{type(txt)}')

    print(txt)
    # print()
    # print('list:')
    # print(list(txt))




if __name__ == '__main__':

    # __teste_read()
    
    write(path='txt.txt', txt='so um teste')


    