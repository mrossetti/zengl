import imageio
import zengl

from window import Window

reader = imageio.get_reader('<video0>')
it = iter(reader)
height, width = next(it).shape[:2]

window = Window(width, height)
ctx = zengl.context()

image = ctx.image(window.size, 'rgba8unorm')

while window.update():
    image.write(zengl.rgba(next(it), 'rgb'))
    image.blit()
