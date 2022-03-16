import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
#font-->way of writing properties--> on titles and labels
'''
fontdict=''-->means we have to creatge a dict which is a key value pair
f1={'family':'arial','size':20,'color':'r'}
plt.title('sample plot',fontdict=f1)
plt.xlabel('',fontdict=f2)
plt.ylabel('',fontdict=f3)
f2={'family':'cambia','color':'b','size':15}
'''
plt.plot(x,y,marker='s',ls='dashed')
f1={'family':'algerian','size':10,'color':'r'}
plt.title('GRAPH',fontdict=f1)
plt.xlabel('x-aixs-->',fontdict=f1)
plt.ylabel('y-axis-->',fontdict=f1)
plt.show()
