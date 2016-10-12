import bpy
from mathutils import Vector, Euler, Matrix

def duplicate(name):
    r"""
    Duplicate the object whose name is given.

    The duplicate is placed on the first layer.
    """
    base = bpy.data.objects[name]
    duplicate = base.copy()
    duplicate.layers = [i == 1 for i in range(len(duplicate.layers))]
    bpy.data.scenes[0].objects.link(duplicate)
    return duplicate

def make_branch(location, angle, size):
    r"""
    Creates a branch.
    
    INPUTS
    
    - ``location``: the origin of the branch
    - ``angle``: the angle of rotation of the branch
    - ``size``: the size of the branch
    """
    direction = Vector((0,0,1))
    branch = duplicate('Branch')
    branch.location = location
    branch.scale *= size
    branch.rotation_euler = Euler((0, angle, 0), 'XYZ')

def make_plant(location, angle, size, depth):
    r"""
    Creates a fractal plant.

    INPUTS
    
    - ``location``: the origin of the plant
    - ``angle``: the angle of rotation of the plant
    - ``size``: the size of the plant
    - ``depth``: the fractal depth
    """
    if depth == 0:
        make_branch(location, angle, size)
    else:
        direction = Matrix.Rotation(angle, 3, 'Y') * (size / 3 * Vector((0,0,1)))
        make_plant(location, angle, size / 3, depth - 1)
        make_plant(location + direction, angle, size / 3, depth - 1)
        make_plant(location + direction, angle + 170, size / 3, depth - 1)
        make_plant(location + 2 * direction, angle, size / 3, depth - 1)
        make_plant(location + 2 * direction, angle - 170, size / 3, depth - 1)

origin = Vector((0,0,0))
make_plant(origin, 0, 3.0, 4)
