import matplotlib.pyplot as plt
import numpy as np
'''line style-->we can change the stylem of lines
line style='s'
shortcut-->ls='solid'-->by default it is solid
dotted --
dashed - - - - -
dashdot -. -. -.
none--line will not appear
the enxt thing is line width
line width-->lw=20
line color-->c=''-->same as markers
'''
x=np.arange(0,10,2)
y1=x**2
y2=x**3
#plt.plot(x,y,marker='p',mfc='b',mec='r',ms='15',ls='none',lw=10,c='r')
#in single plot function we can draw multiple lines
plt.plot(x,y1,x,y2)
plt.xlabel('x-axis-->')
plt.ylabel('y-axis-->')
plt.title('GRAPH')
plt.show()
