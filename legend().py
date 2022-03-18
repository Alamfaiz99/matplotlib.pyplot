from matplotlib import pyplot as plt
import numpy as np
#legend()-->tells the functionality of the graph
'''
y=x**2
y1=x**3
(x,y)-->square
(x,y1)-->cube
this is tell by the legend
legend()-->without parameters
legend()-->with parameter

plot(x,y,label='square')
plot(x,y1,legend='cubel')
plt.legend()



legend(loc=''/0-10,framealpha=''/0-1)
upper left
upper right
lower left
lower right
upper center
lower center
center
0-10 each represent a loc


2.framealpha  0-->transparent
              1-->show
3.facecolor='red' or hexadecimal
4.edgecolor='yellow'name or hexadecimal format
5.shadow=true/false
6fancybox=true/false

legend(label=['square','cubes'],loc=)
'''

x=np.arange(0,10,2)
y=x**2
y1=x**3
'''
plt.plot(x,y,marker='p',ms=10,label='square')
plt.xlabel('x-axis-->')
plt.ylabel('y-axis-->')
plt.title('GRAPH')
plt.legend()
plt.show()
'''
plt.plot(x,y,marker='p',ms=10)
plt.plot(x,y1,marker='s',ms=5)
plt.xlabel('x-axis-->')
plt.ylabel('y-axis-->')
plt.title('GRAPH')
plt.legend(['square','cube'],loc='upper center',framealpha=1,facecolor='yellow',edgecolor='red',fancybox=True)
plt.show()
