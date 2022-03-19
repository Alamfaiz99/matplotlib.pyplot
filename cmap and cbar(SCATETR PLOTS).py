from matplotlib import pyplot as plt
import numpy as np
'''
cmap and colorbar-->in scatter plot in matplotlib.pyplot
how to represent each point with different color

cmap-->an argument in scatter method to put every dot a unique point

colorbar()-->is a method in numplotlib.pyplot which is used to see the numerical vaalue of color

in matplotlib we have colormap which ranges from 0-99
'''

x=[10,20,30,40]
y=[200,400,500,700]
#colors=['b','g','m','y']
colors=[10,20,30,40]

sizes=[40,80,120,60]

#cmap='viridis'
#cmap='Accent'
#cmap='rainbow'

#plt.scatter(x,y)
plt.scatter(x,y,c=colors,s=sizes,cmap='rainbow')
plt.colorbar()
#to see the color value in plott/graph
plt.show()
