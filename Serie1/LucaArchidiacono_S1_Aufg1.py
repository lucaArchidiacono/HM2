# -*- coding: utf-8 -*-
"""
@author: archiluc
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Aufgabe a)
def f(v0,alpha):
    return (v0**2*np.sin(2*(alpha*np.pi/180)))/9.81

[v0,alpha] = np.meshgrid(np.linspace(0,100, 1001), np.linspace(0,90, 1001))

w = f(v0, alpha)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(v0, alpha, w)

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(v0, alpha, w, cmap=cm.coolwarm)
fig.colorbar(surf , shrink=0.5, aspect=5)

fig = plt.figure(3)
cont = plt.contour(v0, alpha, w)

# Maximum wird mit einem Winkel von 45 Grad erreicht. Dies mit einer höchsten Geschwindigkeit von 1000m/s.

plt.title('Höhenlinie')
ax.set_xlabel('v0')
ax.set_ylabel('alpha')
ax.set_zlabel('w')

# Aufgabe b)
R =  8.31
def pFunc(V, T):
    return (R*T)/V

def VFunc(p, T):
    return (R*T)/p

def TFunc(p, V):
    return (p*V)/R

[V,T] = np.meshgrid(np.linspace(0.01,0.2), np.linspace(0.1,1e4))
p = pFunc(V, T)
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(V, T, p)
fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(V, T, p, cmap=cm.coolwarm)
fig.colorbar(surf , shrink=0.5, aspect=5)
fig = plt.figure(6)
cont = plt.contour(V, T, p)

plt.title('p=p(V,T)=RT/V')
ax.set_xlabel('V')
ax.set_ylabel('T')
ax.set_zlabel('p')


[p,T] = np.meshgrid(np.linspace(1e4,1e5), np.linspace(0.1,1e4))
V = VFunc(p, T)
fig = plt.figure(7)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(p, T, V)
fig = plt.figure(8)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(p, T, V, cmap=cm.coolwarm)
fig.colorbar(surf , shrink=0.5, aspect=5)
fig = plt.figure(9)
cont = plt.contour(p, T, V)

plt.title('V=V(p,T)=RT/p')
ax.set_xlabel('p')
ax.set_ylabel('T')
ax.set_zlabel('V')


[p,V] = np.meshgrid(np.linspace(1e4,1e6), np.linspace(0.1,10))
T = TFunc(p, V)
fig = plt.figure(10)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(p, V, T)
fig = plt.figure(11)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(p, V, T, cmap=cm.coolwarm)
fig.colorbar(surf , shrink=0.5, aspect=5)
fig = plt.figure(12)
cont = plt.contour(p, V, T)

plt.title('T=T(p,V)=pV/R')
ax.set_xlabel('p')
ax.set_ylabel('V')
ax.set_zlabel('T')

plt.show()