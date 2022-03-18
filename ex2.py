import matplotlib.pyplot as plt
import numpy as np
#noow lets put gridon the graph/plot
x=np.arange(0,10,2)
y=x**2
y1=x**3
y2=x**4
f1={'family':'algerian','color':'r','size':15}
plt.subplot(1,2,1)
plt.grid(axis='both',ls='dotted',lw=3,c='m')
plt.plot(x,y,marker='s',mfc='r',mec='b',ms=10,ls='dashdot',lw=5,c='r',label='A')
plt.xlabel('X-axis-->',fontdict=f1)
plt.ylabel('Y-axis-->',fontdict=f1)
plt.title('GRAPH1')

plt.subplot(1,2,2)
plt.grid(axis='both',ls='solid')
plt.plot(x,y1,marker='s',mfc='r',mec='b',ms=10,ls='dashdot',lw=5,c='r',label='A')
plt.xlabel('X-axis-->',fontdict=f1)
plt.ylabel('Y-axis-->',fontdict=f1)
plt.title('GRAPH2')
plt.suptitle('GRAPHS')
plt.legend(loc='upper center')
plt.show()

