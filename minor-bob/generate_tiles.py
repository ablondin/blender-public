import bpy
from math import pi

for obj in bpy.data.objects:
    if obj.name.startswith('Tile'):
        tokens = obj.name.split('.')
        num_rotations = int(tokens[1])
        name = tokens[2].lower()
        obj.location[0] = 0
        obj.location[1] = 0
        for r in range(num_rotations):
            bpy.context.scene.render.filepath = 'tiles/tile-%s-%s.png' % (name, r)
            obj.rotation_euler[2] = r * pi / 2
            bpy.ops.render.render(write_still=True)
        obj.hide_render = True
