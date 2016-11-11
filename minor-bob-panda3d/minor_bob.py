from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import *
 
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
 
        # Load the environment model.
        self.scene = self.loader.loadModel("assets/models/scene")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)

        # Load Bob
        self.bob = Actor("assets/models/bob",
                         {"walk": "assets/models/bob-Walk"})
        self.bob.setPos(0, 0, 1)
        self.bob.reparentTo(self.render)
        self.bob.loop("walk")

        # Lights
        ambient_light = AmbientLight('ambiant')
        ambient_light.setColor(Vec4(0.8, 0.8, 0.8, 1))
        alnp = render.attachNewNode(ambient_light)
        alnp.setHpr(30, -30, 0)
        self.render.setLight(alnp)

        directional_light = DirectionalLight('dlight')
        directional_light.setColor(VBase4(0.8, 0.8, 0.5, 1))
        dlnp = self.render.attachNewNode(directional_light)
        dlnp.setHpr(0, -60, 0)
        self.render.setLight(dlnp)
 
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(5 * sin(angleRadians), -5.0 * cos(angleRadians), 5)
        self.camera.setHpr(angleDegrees, -40, 0)
        return Task.cont
 
app = MyApp()
app.run()
