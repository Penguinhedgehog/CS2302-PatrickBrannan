import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):            
  n = int(4*rad*math.pi)    
  t = np.linspace(0,6.3,n)
  x = center[0]+rad*np.sin(t) 
  y = center[1]+rad*np.cos(t)
  return x,y

def circle_ception(ax, n, center_x, center_y, radius, w):  #Creates repititous circles
    if n > 0:
        center = [center_x, center_y]
        x, y = circle(center, radius)
        ax.plot(x, y, color='k')

        circle_ception(ax, n-1, center_x, center_y, radius*w, w)  #Creates the circle in the middle

        q,t = center_x - radius*(1-w), center_y   
        circle_ception(ax,n-1,q,t,radius*w,w)       #Circles on the left

        q,t = center_x+radius*(1-w), center_y              
        circle_ception(ax,n-1,q,t,radius*w,w)       #circles on the right

        q,t = center_x, center_y-radius*(1-w)
        circle_ception(ax,n-1,q,t,radius*w,w)       #circles on the bottom
        q,t = center_x, center_y+radius*(1-w)
        circle_ception(ax,n-1,q,t,radius*w,w)       #circles on the top


plt.close("all") 
fig, ax = plt.subplots()

circle_ception(ax, 4, 100,100, 100, .3333333)  #sets up circle_ception

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
