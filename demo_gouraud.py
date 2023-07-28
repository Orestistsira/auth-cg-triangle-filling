import time
import matplotlib.pyplot as plt
import numpy as np

from render import render


# load data
data = np.load('h1.npy', allow_pickle=True)[()]

verts2d = data['verts2d']
vcolors = data['vcolors']
faces = data['faces']
depth = data['depth']
shade_t = "gouraud"

print(verts2d)
print(depth)

print('Rendering model with shading method "' + str(shade_t) + '"...')
start_time = time.time()

# render triangles
img = render(verts2d, faces, vcolors, depth, shade_t)

print('Model successfully rendered in %.2fs' % (time.time() - start_time))

plt.imsave('gouraud.png', np.array(img[::-1]))
