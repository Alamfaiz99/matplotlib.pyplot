from matplotlib import pyplot as plt
import numpy as np
'''
scatter plot-->patches plot circular patches plot
scatter()-->function
plt.scatter(x,y,c=)-->blue
plt.scatter(x,y1,c='red',marker='0,*,^-->triange',s=15,,linewidth=10,alpha='0/1'-->inbw 0-1 any float number transparency)-->ortange
^-->trianle marker
'''
x=np.arange(0,10,2)
y=x**2
plt.scatter(x,y,c='r',marker='^',s=10,lw=10,alpha=0.1)
plt.show()
