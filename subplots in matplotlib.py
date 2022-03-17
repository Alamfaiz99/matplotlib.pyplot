'''
subplots in matplotylib
subplot()-->it is is function in matplotlib.pyplot
subplot()-->is used to represent multiple figues in a graph
figure-->is a place where we are drawing the plots
subplot means in same figure we are drawing multiple figures


subplot(R,C,I)
R=row
C=column
I=index of plot
no. of plots=R*c


----1---|-----2------
subplot(1,2,1)
subplot(1,2,2)

         |
         |subplot(2,1,1)
  -------1-----------       |
         |
         |subplot(2,1,2)
  -------2------------
         |
         |
         |
now

        subplot(2,2,1)
        plot()
------|1----------|2--------
      |          |subplot(2,2,2)
      |          |plot()
      |          |
      |subplot(2,2,3)          |
-------3---------4|--------
      |          |subplot(2,2,4)

suptitle('')-->supertitle
'''
from matplotlib import pyplot as plt
import numpy as np
x=[1,2,3,4]
y=[10,20,30,40]
y1=[13,54,90,34]
y2=[10,20,32,87]
y3=[14,27,39,40]
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title('plot1')
plt.subplot(2,2,2)
plt.plot(x,y1)
plt.title('plot2')
plt.subplot(2,2,3)
plt.plot(x,y2)
plt.title('plot3')
plt.subplot(2,2,4)
plt.plot(x,y3)
plt.title('plot4')
plt.suptitle("GRAPHS")
plt.show()
