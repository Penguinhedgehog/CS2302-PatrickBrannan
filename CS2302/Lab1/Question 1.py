import numpy as np
import matplotlib.pyplot as plt

def corner_squares(ax,n,p):
  if n>0:
    i1 = [1,2,3,0,1]
    ax.plot(p[:,0],p[:,1],color='k')
    
    q = -250 + p[i1]*.5          #coordinates for bottom left
    corner_squares(ax,n-1,q)
    
    q = 750 + p[i1]*.5           #coordinate for top right
    corner_squares(ax,n-1,q)
    
    q = [-250, 750] + p[i1]*.5   #coordinate for top left
    corner_squares(ax,n-1,q)
    
    q = [750, -250] + p[i1]*.5   #coordinate for bottom right
    corner_squares(ax,n-1,q)
    

plt.close("all")
base = 1000                      #Creates the base size of the square
p = np.array([[0,0], [0, base], [base, base], [base, 0], [0, 0]])
fig, ax = plt.subplots()

corner_squares(ax, 4, p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

#n = number of squares
#p = coordinates/lines to make the square
#w- percantage at which the new points are chosen