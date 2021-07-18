from ursina import *


class teste_de_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45, 45, 45) 
            
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
        
def update(): # update eh do proprio URSINA, não funciona de outro jeito

    if held_keys['a']:
    
        teste_de_square.x -= 2 * time.dt
    if held_keys['d']:
        teste_de_square.x += 2 * time.dt

    if held_keys['w']:
        teste_de_square.y += 2*time.dt     
    if held_keys['s']:
        teste_de_square.y -= 2*time.dt

app = Ursina()


teste_de_square = Entity(model = 'cube', color = color.red, scale=(1,3), position=(3,1))

jonas_texture = load_texture('boy.png')
jonas = Entity(model = 'quad', texture=jonas_texture)

teste_de_cube = Teste_de_botao()


app.run()

