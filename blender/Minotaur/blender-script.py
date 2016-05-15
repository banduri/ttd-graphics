

import bpy
from bpy import *
#from bpy.Scene import Render

pi = 3.14159
deg45 = 45 * pi / 180

step_count = 8
platform = bpy.data.scenes[0].objects["RenderPlatform"]

step = 1

platform.rotation_euler[2] = deg45 * step
bpy.context.scene.render.filepath = '/tmp/foo_%s' %str(step)
bpy.ops.render.render()
