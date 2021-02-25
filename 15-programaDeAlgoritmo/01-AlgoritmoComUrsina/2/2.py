from ursina import *
from random import *

class teste_de_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'quad',
            color = color.white,
            #texture = 'white_cube',
            #rotation = Vec3(35, 45, 45) 
            
        )
class Teste_de_botao(Button):
    def __init__(self):
        super().__init__(
            
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('botao apertado / button pressed')
        
#def update(): # update eh do proprio URSINA, não funciona de outro jeito
#
#    if held_keys['a']:
#    
#        teste_de_square.x -= 2 * time.dt
#    if held_keys['d']:
#        teste_de_square.x += 2 * time.dt
#
#    if held_keys['w']:
#        teste_de_square.y += 2*time.dt     
#    if held_keys['s']:
#        teste_de_square.y -= 2*time.dt



app = Ursina()

algo = [i for i in range(1, 6)]
print(algo)

shuffle(algo)
filas = []
for i, n in enumerate(algo):
    filas[i] = Entity(model = 'quad', color = color.red, scale=(1,n), position=(i-6, 0))
    
def M2(lista):
    guardarNumero = 0
    for i, n in enumerate(lista):
        if i != len(lista):
            if lista[i] > lista[1+i]:
                guardarNumero = lista[1+i]
                lista[1+i] = lista[i]
                lista[i] = guardarNumero
                filas[i] = Entity(model = 'quad', color = color.red, scale=(1,n), position=(i-6, 0))


M2(algo)
#teste_d = Entity(model = 'cube', color = color.blue, scale=(1,4), position=(4,0))


teste_de_cube = Teste_de_botao()


app.run()

