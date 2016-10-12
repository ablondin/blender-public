import bpy
from mathutils import Vector
from random import randint, choice

def make_material(name, diffuse, specular, alpha):
    material = bpy.data.materials.new(name)
    material.diffuse_color = diffuse
    material.diffuse_shader = 'LAMBERT'
    material.diffuse_intensity = 1.0
    material.specular_color = specular
    material.specular_shader = 'COOKTORR'
    material.specular_intensity = 0.5
    material.alpha = alpha
    return material

materials = [make_material('red',     (1,0,0), (1,1,1), 1),\
             make_material('green',   (0,1,0), (1,1,1), 1),\
             make_material('blue',    (0,0,1), (1,1,1), 1),\
             make_material('yellow',  (1,1,0), (1,1,1), 1),\
             make_material('magenta', (1,0,1), (1,1,1), 1),\
             make_material('cyan',    (0,1,1), (1,1,1), 1)]

xmin = -8
xmax = 8
ymin = -8
ymax = 8

for x in range(xmin, xmax + 1):
    for y in range(ymin, ymax + 1):
        height = randint(1, 5)
        for z in range(1, height + 1):
            material = choice(materials)
            bpy.ops.mesh.primitive_cube_add(location=(x,y,z),\
                                            layers=[True] + [False] * 19)
            cube = bpy.context.active_object
            cube.scale = Vector((0.5, 0.5, 0.5))
            cube.data.materials.append(material)
