import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center, rad):
  n = int(4*rad*math.pi)    
  t = np.linspace(0,6.3,n)      #Can splice the circle with multiplication
  x = center[0] + rad*np.sin(t)   #can squish by multiplying (width)
  y = center[1] + rad*np.cos(t)   #Can squish by multiplying (height)
  return x, y

def draw_circles(ax, n, center, radius, w, base):
  if n>0:
    x,y = circle(center,radius)
    ax.plot(x, y, color='k')
    base = base*w
    draw_circles(ax, n-1, [base, 0], radius*w, w, base)


plt.close("all") 
fig, ax = plt.subplots()

draw_circles(ax, 100, [100,0], 100, .9, 100)    #Sets up draw_circles

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

#I Used the example of Squares and circles as a base for questions 1 and 2