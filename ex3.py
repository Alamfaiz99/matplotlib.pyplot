import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
y1=x**3
f1={'family':'algerian','color':'b','size':10}
plt.grid(axis='both',ls='dotted',lw=5,c='b')
plt.subplot(1,2,1)
#plt.plot(x,y,marker='^',mfc='b',mec='r',ms=10,ls='dashed',lw=10,c='m')
plt.scatter(x,y,c='b',marker='*',alpha=0.99)
plt.xlabel("x-axis-->",fontdict=f1)
plt.ylabel("y-axis-->",fontdict=f1)
plt.title("GRAPH1",fontdict=f1)

plt.subplot(1,2,2)
plt.plot(x,y1,marker='s',mfc='b',mec='r',ms=10,ls='dashed',lw=10,c='m')
plt.xlabel("x-axis-->",fontdict=f1)
plt.ylabel("y-axis-->",fontdict=f1)
plt.title("GRAPH2",fontdict=f1)


plt.legend(['square','cube'],loc='upper center',framealpha=1,facecolor='y',edgecolor='r',fancybox=True)
plt.suptitle("GRAPHS")

plt.show()
