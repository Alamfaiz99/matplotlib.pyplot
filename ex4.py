import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,2)
y=x**2

#plt.plot(x,y,marker='s',mfc='r',mec='b',ls='dotted',lw=4,c='m',label='SQUARE')\
'''
colors=['r','b','g','m','g']
sizes=[100,200,350,109,780]
plt.scatter(x,y,c=colors,s=sizes,alpha=0.9)
plt.grid(axis='both',ls='dotted',lw=5,c='r')
plt.colorbar()
f1={'family':'algerian','color':'r','size':10}
plt.xlabel('x-axis-->',fontdict=f1)
plt.ylabel('y-axis-->',fontdict=f1)
plt.title('GRAPH',fontdict=f1)
plt.show()
'''
#horizontal and vertical bargraph
#bar()-->vertical bar graph
#barh()-----for horizontal bargraph
x=[10,20,30,40]
y=[1,2,3,4]
plt.bar(x,y,color='r',width=0.8,label="square")
plt.barh(x,y,height=0.8)
plt.legend()
plt.show()
