import matplotlib.pyplot as plt
import numpy as np
#numpy is a pak
#ckage which is use to go scientific computation in python
x=np.arange(0,10,2)
y=x**2
f1={'family':'algerian','color':'r','size':15}
f2={'family':'arial','color':'r','size':20}
plt.rcParams['figure.figsize']=[7.5,3.5]
plt.rcParams['figure.autolayout']=True
plt.plot(x,y,marker='p',mfc='r',mec='b',ms=10,ls='dashed',lw=5,c='g',label='A')
plt.xlabel('x-axis-->',fontdict=f1)
plt.ylabel('y-axis-->',fontdict=f1)
plt.title('GRAPH',fontdict=f2)
plt.legend(loc='upper center')
plt.show()
