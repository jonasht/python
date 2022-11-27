from ursina import *



def update(): # update eh do proprio URSINA, não funciona de outro jeito

    teste_de_square.x -= 1 
 
app = Ursina()


teste_de_square = Entity(model = 'cube', color = color.green, scale=(1,5), position=(6,1))


app.run()

