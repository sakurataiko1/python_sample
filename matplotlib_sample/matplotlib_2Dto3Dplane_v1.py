# 参考：https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html#sphx-glr-gallery-mplot3d-pathpatch3d-py
# 参考：https://sabopy.com/py/matplotlib-3d-43/
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Rectangle


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Draw a circle on the x=0 'wall'
#p = Circle((5, 5), 3)
pLeftRight = Rectangle(xy=(0, 0), width=2, height=5 ,fc='g',ec='g',alpha=0.5)
ax.add_patch(pLeftRight)
art3d.pathpatch_2d_to_3d(pLeftRight, z=0, zdir="x")

pFrontBack = Rectangle(xy=(0, 0), width=5, height=2 ,fc='g',ec='g',alpha=0.5)
ax.add_patch(pFrontBack)
art3d.pathpatch_2d_to_3d(pFrontBack, z=0, zdir="y")


pTopBottom = Rectangle(xy=(0, 6), width=8, height=3 ,fc='g',ec='g',alpha=0.5)
ax.add_patch(pTopBottom)
art3d.pathpatch_2d_to_3d(pTopBottom, z=0, zdir="z")


ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

plt.show()