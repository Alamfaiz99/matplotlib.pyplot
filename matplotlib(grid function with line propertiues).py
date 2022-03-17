import matplotlib.pyplot as plt
import numpy as np
#grid function with line properties
'''
grid function will give line on both x axis and y axis
^
|--|--|--|--|--|
|--|--|--|--|--|
|--|--|--|--|--|
|--|--|--|--|--|
|--|--|--|--|--|
|____________________>
this is known as grid
means it will create lines on x axis as well as y axis
grid()-->get gridlines on the graph/chart
grid(axis='x')
grids will appply only on the x axis
literal meaning-->aa collection of horizontl and vertical lines
grid-->to divide axis into parts
grid(axis='both')-->grid will apply both on x axis and y axis

grids are lines-->so we can apply line properties
lw=''-->line width
ls=''-->line style
c=''-->color

grid(axis='both,ls='dotted',lw=10,c='b')
'''
x=np.arange(0,10,2)
y=x**2
plt.grid(axis='both')
#plt.grid(axis='both',ls='dotted',lw=2,c='m')
plt.plot(x,y,marker='s',mfc='b',mec='r',ms=10,ls='dashdot',lw=10,c='g',label='A')
plt.xlabel('X-axis-->')
plt.ylabel('Y-axis-->')
plt.title('GRAPH')
plt.show()
