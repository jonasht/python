from ursina import *



def update(): # update eh do proprio URSINA, não funciona de outro jeito

    if held_keys['a']:
    
        teste_de_square.x -= 1 * time.dt
    if held_keys['d']:
        teste_de_square.x += 1 * time.dt
app = Ursina()


teste_de_square = Entity(model = 'cube', color = color.green, scale=(1,5), position=(6,1))


app.run()

