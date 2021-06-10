from ursina import *



def update(): # update eh do proprio URSINA, não funciona de outro jeito

    if held_keys['a']:
    
        teste_de_square.x -= 2 * time.dt
    if held_keys['d'] or held_keys['left']:
        teste_de_square.x += 2 * time.dt

    if held_keys['w']:
        teste_de_square.y += 2*time.dt     
    if held_keys['s']:
        teste_de_square.y -= 2*time.dt

app = Ursina()


teste_de_square = Entity(model = 'cube', color = color.red, scale=(1,3), position=(0,1))


app.run()

