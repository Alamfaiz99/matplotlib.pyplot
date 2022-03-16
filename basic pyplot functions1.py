import matplotlib.pyplot as plt
import numpy as np
#np.arange(0,10,2)-->starting with 0 with a multiple of 2 till 8
#and 10 is exclusive it is present in numpy
#which is a numerical python
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker='*',mfc='r',mec='b',ms=10,label='A')
#These rae default arguments available in plot()
#you should learn all these things thats very important
#mfc=marker face color
#mec=bounday-->marker edge color
#ms=10
#label=to recoginse a particular graph uniquely
plt.xlabel('x-axis-->')
plt.ylabel('y-axis-->')
plt.title('GRAPH')
plt.legend(loc='upper center')
plt.show()
