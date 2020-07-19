from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
window.title = 'jogo'
window.fullscreen = True

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.green,
            highlight_color = color.yellow,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)
for z in range(50):
    for x in range(50):
        voxel = Voxel(position=(x,0,z))


player = FirstPersonController()
app.run()
