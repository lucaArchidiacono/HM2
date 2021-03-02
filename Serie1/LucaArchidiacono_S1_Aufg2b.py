# -*- coding: utf-8 -*-
"""
@author: archiluc
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import scipy.constants as con

def w(x,t):
    return np.sin(x+t)
x = np.arange(1,6,0.1)
t = np.arange(1,6,0.05)
x, t = np.meshgrid(x,t)
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
z = w(x, t)
Axes3D.plot_wireframe(ax, x, t, z, rstride=10, cstride=10)

def v(x,t):
    return np.sin(x+t)+np.cos(2*x+2*t)
x = np.arange(1,6,0.1)
t = np.arange(1,6,0.05)
x, t = np.meshgrid(x,t)
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
z = v(x, t)
Axes3D.plot_wireframe(ax, x, t, z, rstride=10, cstride=10)

plt.show()